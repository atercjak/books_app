from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    email = forms.CharField(label='Adres email')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise ValidationError("Hasła nie są identyczne")

        return password_confirmation

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
        )
        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        fields = ('email', 'password')

    error_messages = {
        "invalid_login": "Email użytkownika lub hasło są nieprawidłowe"
    }
