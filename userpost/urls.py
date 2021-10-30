from django.urls import path
from userpost import views


urlpatterns = [
    # path("posts/", views.posts_list),
    # path("posts/<int:pk>/", views.post_detail),
]

urlpatterns += [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
