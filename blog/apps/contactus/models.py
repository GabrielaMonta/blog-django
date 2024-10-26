from django.db import models

# Create your models here.

class Contactus(models.Model):
    name_contact = models.CharField(max_length=100)
    email_contact = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_contact} - {self.subject}"