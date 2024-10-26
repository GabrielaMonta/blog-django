from django.contrib import admin
from apps.contactus.models import Contactus

# Register your models here.

@admin.register(Contactus)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_contact', 'email_contact', 'subject', 'message')
