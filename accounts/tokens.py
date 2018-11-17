from datetime import datetime

from django.conf import settings
from django.contrib.auth.tokens import (
    PasswordResetTokenGenerator as BasePasswordResetTokenGenerator
)
from django.utils.crypto import constant_time_compare
from django.utils.http import base36_to_int


class PasswordResetTokenGenerator(BasePasswordResetTokenGenerator):

    def make_token(self, user):
        return self._make_token_with_timestamp(user, self._num_hours(self._hour()))

    def check_token(self, user, token):
        if not (user and token):
            return False
        try:
            ts_b36, hash = token.split("-")
        except ValueError:
            return False
        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False
        if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):
            return False

        if (self._num_hours(self._hour()) - ts) > settings.PASSWORD_RESET_TIMEOUT_HOURS:
            return False

        return True

    def _num_hours(self, dt):
        return int((dt - datetime(2001, 1, 1, 0, 0, 0)).total_seconds() / 60 / 60)

    def _hour(self):
        return datetime.now().replace(minute=0, second=0, microsecond=0)


default_token_generator = PasswordResetTokenGenerator()
