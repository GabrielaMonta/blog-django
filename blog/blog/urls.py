"""
URL configuration for blog project.
The `urlpatterns` list routes URLs to views. For more information please see:
 https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
 1. Add an import: from my_app import views
 2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
 1. Add an import: from other_app.views import Home
 2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
 1. Import the include() function: from django.urls import include, path
 2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.views import IndexView, AboutView, ContactView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('posts/', include('apps.post.urls', namespace='post')),
    path('users/', include('apps.user.urls', namespace='user')),
    path('section/about/', AboutView.as_view(), name='section_about'),
    path('section/contact/', ContactView.as_view(), name='section_contact'),
    path('contactuss/', include('apps.contactus.urls', namespace='contactus')),
]

if settings.DEBUG:
 from django.conf.urls.static import static
 # Sirviendo archivos estáticos
 urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
 # Sirviendo archivos media
 urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
 
