from django.views.generic import TemplateView
from apps.post.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = Post.objects.all().order_by('-creation_date')[:3]
        context['count_comments'] = Post.objects.all().count()
        return context


class AboutView(TemplateView):
    template_name = 'sections/about.html'


class ContactView(TemplateView):
    template_name = 'sections/contact.html'


class AuthLoginView(TemplateView):
    template_name = 'auth/auth_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['color_bg_form'] = 'bg-[#451121]'
        context['color_bg'] = 'bg-[#DCA278]'
        return context


class AuthRegisterView(TemplateView):
    template_name = 'auth/auth_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['color_bg_form'] = 'bg-[#3D190C]'
        context['color_bg'] = 'bg-[#DCA278]'
        return context
