from django.urls import path
from .views import post_list, post_detail


urlpatterns = [
    path('', post_list, name='posts'),
    path('post-detail/<int:pk>', post_detail, name='post-detail'),
]
