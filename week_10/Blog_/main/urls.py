from django.urls import path
from . import views

urlpatterns=[
    path('post/',views.PostListView.as_view(),name = "post"),
    path('MyPost/',views.MyPostListView.as_view(),name = "my_post"),
    path('home/',views.home,name="home"),
    path('post/create/',views.PostCreateView.as_view(),name = 'create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name = "update"),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name = "delete"),
    path('post/<int:pk>/comment/',views.PostCommentCreateView.as_view(),name = "comment_add"),
    path('post/comments/',views.CommentDetailView.as_view(),name = "comment"),
    path('comment/<int:pk>/update/',views.CommentUpdateView.as_view(),name = "update_com"),
    path('comment/<int:pk>/delete/',views.CommentDeleteView.as_view(),name = "delete_com"),

]