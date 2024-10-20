from django.urls import path
import apps.post.views as views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('comments/<uuid:pk>/update/', views.CommentUpdateView.as_view(),
        name='comment_update'),
    path('comments/<uuid:pk>/delete/', views.CommentDeleteView.as_view(),
        name='comment_delete'),
    path('posts/<slug:slug>/comments/create/', views.CommentCreateView.as_view(),
        name='comment_create'),
]

