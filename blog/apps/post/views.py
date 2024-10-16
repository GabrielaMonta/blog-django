


# from apps.post.models import Post


# class PostListView(ListView):
# model = Post
# template_name = 'post/post_list.html'
# context_object_name = 'posts'


from django.views.generic import TemplateView, ListView, CreateView, DetailView
from apps.post.models import Post, PostImage 
from apps.post.forms import NewPostForm 
from django.urls import reverse 
from django.conf import settings 



class PostUpdateView(TemplateView):
    template_name = 'post/post_update.html'


class PostDeleteView(TemplateView):
    template_name = 'post/post_delete.html'

#Listar posts
class PostListView(ListView): 
    model = Post 
    template_name = 'post/post_list.html' 
    context_object_name = 'posts'

#Crear post
class PostCreateView(CreateView): 
    model = Post 
    form_class = NewPostForm 
    template_name = 'post/post_create.html' 

    def form_valid(self, form): 
        form.instance.author = self.request.user 
        post = form.save() 

        images = self.request.FILES.getlist('images') 

        if images: 
            for image in images: 
                PostImage.objects.create(post=post, image=image) 
        else: 
            PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE) 
    
        return super().form_valid(form) 
    
    def get_success_url(self): 
        return reverse('post:post_detail', kwargs={'slug': self.object.slug}) 
    
#Ver un post en detalle
class PostDetailView(DetailView): 
    model = Post 
    template_name = 'post/post_detail.html' 
    context_object_name = 'post'

'''
Sera necesario definir luego el metodo get_context_data para poder pasar las
imagenes del post a la plantilla.
'''