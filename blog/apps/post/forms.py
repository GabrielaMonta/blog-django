from django import forms 
from apps.post.models import Post, PostImage 

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ('title', 'content', 'allow_comments') 

class NewPostForm(PostForm): 
    image = forms.ImageField(required=False) 

    def save(self, commit=True): 
        post = super().save(commit=False)  
        image = self.cleaned_data['image']
        
        if commit: 
            post.save()  # Guardamos el post
            if image:  # Si hay una imagen
                PostImage.objects.create(post=post, image=image)  # Creamos la relación de PostImage con la imagen
        
        return post  # Retornamos el post al final del método

class UpdatePostForm(PostForm): 
    pass
