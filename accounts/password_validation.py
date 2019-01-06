from django.core.exceptions import ValidationError


class LengthValidator:

    def __init__(self, min_length=8, max_length=20):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        if not self.min_length <= len(password) <= self.max_length:
            raise ValidationError(
                'パスワードは{0}文字以上{1}文字以下にしてください'.format(
                    self.min_length, self.max_length
                )
            )

    def get_help_text(self):
        return 'パスワードは{0}文字以上{1}文字以下です'.format(
            self.min_length, self.max_length
        )
