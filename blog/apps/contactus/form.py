from django import forms
from apps.contactus.models import Contactus

class ContactForm(forms.ModelForm):
    name_contact = forms.CharField(
        label="Nombre",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su nombre", "class": "form-control"}
        ),
    )
    email_contact = forms.EmailField(
        label="Correo electrónico",
        max_length=254,
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese su email", "class": "form-control"}
        ),
    )
    subject = forms.ChoiceField(
        label="Razón",
        choices=[
            ('consulta', 'Consulta'),
            ('soporte', 'Soporte Técnico'),
            ('otros', 'Otros'),
        ],
        widget=forms.Select(
            attrs={"placeholder": "Elegir razón", "class": "form-control"}
        ),
        required=True,
    )
    message = forms.CharField(
        label="Mensaje",
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe tu mensaje aquí..."}),
    )

    class Meta:
        model = Contactus
        fields = ['name_contact', 'email_contact', 'subject', 'message']