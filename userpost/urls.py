from django.urls import path
from userpost import views

urlpatterns = [
    path("posts/", views.posts_list),
    path("posts/<int:pk>/", views.post_detail),
]
