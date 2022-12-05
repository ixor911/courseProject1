from django.contrib.auth.forms import UserCreationForm, forms
from . import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password1', 'password2', 'image', 'place', 'gender', 'other']





