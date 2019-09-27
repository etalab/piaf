from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
        labels = {
            'username': "Nom d'utilisateur",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
