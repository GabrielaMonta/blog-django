from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'     
    })

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
        # Django form trabaja con widgets
        # Los widgets son los elementos que se renderizan en el HTML
        # Pueden recibir atributos como clases, id, placeholder, etc
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )

