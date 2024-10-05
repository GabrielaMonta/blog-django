from django.views.generic import TemplateView


class PostDetailView(TemplateView):
    template_name = 'post/post_detail.html'


class PostUpdateView(TemplateView):
    template_name = 'post/post_update.html'


class PostDeleteView(TemplateView):
    template_name = 'post/post_delete.html'
