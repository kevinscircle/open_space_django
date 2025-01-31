from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.CreatePostView.as_view(), name='post_create'),
    path('details/<int:pk>/', views.PostDetailsView.as_view(), name='post_detail'),  # Detail page for a single post.
    path('update/<int:pk>/', views.PostUpdateView2.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('comments/', views.CommentListView.as_view(), name='comment_list'),  # Update page for a single post.
]