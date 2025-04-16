from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_info/" , views.post_info),
    path("add_post/" , views.add_post),
    path("my_posts/post_red/", views.post_red),
    path("my_posts/", views.my_posts),

]