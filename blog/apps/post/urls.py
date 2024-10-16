from django.urls import path
import apps.post.views as views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', views.PostDeleteView.as_view(), name='post_delete')
]

