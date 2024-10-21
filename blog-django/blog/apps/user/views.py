from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from apps.user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth import login

class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        # Llama al contexto de la clase padre
        context = super().get_context_data(**kwargs)
        # Agrega el usuario actual al contexto
        context['user_profile'] = self.request.user
        return context
    

class RegisterView(CreateView):
    template_name = 'auth/auth_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')  # Redirige al home una vez registrado

    def form_valid(self, form):
        # Llama a la función form_valid de la clase padre y guarda el usuario
        response = super().form_valid(form)
        
        #inicia sesion automaticamente
        user = form.save()
        login(self.request, user)

        # Asignar el grupo 'Registered' al usuario recién creado
        registered_group = Group.objects.get(name='Registered')
        self.object.groups.add(registered_group)

        # En caso de ser necesario, se le puede asignar explícitamente los permisos del grupo al usuario
        # for permission in registered_group.permissions.all():
        #     self.object.user_permissions.add(permission)

        return response
    '''
    def form_invalid(self, form):
        # Aquí puedes manejar la lógica cuando el formulario es inválido
        return super().form_invalid(form)  # Esto volverá a mostrar el formulario con errores
    '''

class LoginView(LoginViewDjango):
    template_name = 'auth/auth_login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutView(LogoutViewDjango):
    def get_success_url(self):
        return reverse_lazy('home')