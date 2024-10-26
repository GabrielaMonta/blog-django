from django.urls import path
import apps.contactus.views as views

app_name = 'contactus'

urlpatterns = [
    path('', views.ContactoUsuario.as_view(), name='user_contactus'),
]

