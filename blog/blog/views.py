from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


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