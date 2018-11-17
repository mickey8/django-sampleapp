from django.core.exceptions import ValidationError


class LengthValidator:

    def __init__(self, min_length=8, max_length=20):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        if not self.min_length <= len(password) <= self.max_length:
            raise ValidationError(
                'パスワードは%d文字以上%d文字以下にしてください' % (
                    self.min_length, self.max_length
                )
            )

    def get_help_text(self):
        return 'パスワードは%d文字以上%d文字以下です' % (
            self.min_length, self.max_length
        )
