from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md bg-white text-black'
            })
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso.")
        return username


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
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("No hay ningún usuario registrado con ese nombre.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        username = self.cleaned_data.get("username")

        if username and password:
            # Autenticar al usuario con ambos campos
            user = authenticate(username=username, password=password)
            if user is None:
                # Asocia el error al campo de la contraseña
                raise forms.ValidationError("Contraseña incorrecta.")

        return password


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar'] 
       
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field_name in ['first_name', 'last_name', 'email']:
            self.fields[field_name].widget.attrs.update({
                'class': 'border border-gray-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-300 max-w-xs w-full h-10'
            })

