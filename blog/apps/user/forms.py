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
            attrs={'class': 'form-control', 'placeholder': 'Usuario'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'}
        )
    )

    def __init__(self, *args, **kwargs):  # El método debe tener doble guion bajo al principio y al final
        super(LoginForm, self).__init__(*args, **kwargs)
        # Actualizando atributos de los campos
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'
        })

