from apps.contactus.form import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contactus
from django.http import HttpResponseRedirect

class ContactoUsuario(CreateView):
    template_name = 'sections/otro.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactus:user_contactus')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
    
    def form_valid(self, form):
        name_contact = form.cleaned_data['name_contact']
        email_contact = form.cleaned_data['email_contact']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']



        # Agrega el mensaje de éxito
        messages.success(self.request, 'Consulta enviada correctamente.')

        return super().form_valid(form)