from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.CreatePostView.as_view(), name='post_create'),
    path('details/<int:pk>/', views.PostDetailsView.as_view(), name='post_detail'),  # Detail page for a single post.
]