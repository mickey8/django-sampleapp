from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm, UsernameField
)

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nickname', )
        field_classes = {'email': UsernameField, 'nickname': UsernameField}
