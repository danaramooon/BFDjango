from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.HomeView.as_view(),name="home"),
    path('posts/',views.PostListView.as_view(),name="post"),
    path('my_posts/',views.MyPostListView.as_view(),name="my_post"),
    path('posts/add_new/',views.PostCreateView.as_view(),name = "create"),
    path('posts/<int:post_pk>/comments/',views.PostDetailView.as_view(),name="post_detail"),
    path('posts/<int:pk>/comments/add_new',views.CommentCreateView.as_view(),name="add_comment"),
    path('posts/<int:pk>/delete/',views.PostDeleteView.as_view(),name = "delete"),
    path('posts/<int:pk>/update/',views.PostUpdateView.as_view(),name = "update"),
    path('posts/comment/<int:pk>/delete/',views.CommentDeleteView.as_view(),name = "delete_com"),
    path('posts/comment/<int:pk>/update/',views.CommentUpdateView.as_view(),name = "update_com"),
]