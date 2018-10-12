from django.urls import path
from main import views

urlpatterns=[
    path('posts/',views.post_detail,name = "post"),
    path('comments/',views.comment,name = "comment"),
    path('home/',views.home,name = "home"),
    path('<int:pk>/update', views.update_post),
    path('<int:pk>/delete', views.delete_post),
    path('home/add_post/', views.add_post,name = 'add_post'),
]

