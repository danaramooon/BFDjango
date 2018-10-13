from django.urls import path
from main import views

urlpatterns=[
    path('posts/',views.post_detail,name = "post"),
    path('posts/comments/add_comments',views.add_comment,name = "add_comment"),
    path('home/',views.home,name = "home"),
    path('home/add_post/', views.add_post,name = 'add_post'),
    path('posts/<int:id>/update/',views.update_post,name = "update_post"),
    path('posts/<int:id>/delete/',views.delete_post,name = "delete_post"),
    path('posts/<int:id>/comments/',views.comments,name = "comments"),
    path('comments/<int:id>/update/',views.update_comment,name = "update_comment"),
    path('comments/<int:id>/delete/',views.delete_comment,name = "delete_comment"),

]

