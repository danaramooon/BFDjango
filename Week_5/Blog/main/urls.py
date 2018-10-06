from django.urls import path,re_path
from main import views

urlpatterns = [
    path('posts/', views.posts, name = "post"),
    path('posts/comments/', views.comments,name = "comments"),
    path('new_post/',views.add_post,name = "add_post")
  ]
