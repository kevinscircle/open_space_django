from django.urls import path
from .views import ProfileView, ProfileUpdateView, ProductListView



urlpatterns=[
    # path('profile/',views.index,name='index'),
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('product/', ProductListView.as_view(), name='product'),
]


# test