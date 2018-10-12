from django.urls import path,re_path
from main import views

urlpatterns = [
    path('todos/', views.todos, name = "todos"),
    path('todos/1/completed/', views.completed_todos,name = "completed_todos"),
    re_path(r'^todos/([\w\_?]+)/order_by/$', views.todo_filter, name='order_by'),
    re_path(r'^todos/completed/([\w\_?]+)/order_by/$', views.completed_todo_filter, name='completed_order_by'),
    path('new/',views.add_new,name="new_add"),
    re_path(r'^todos/(\d+)/change_mark/$',views.change_button,name="change_button"),
    re_path(r'^todos/(\d+)/delete/$',views.delete,name="delete"),
    re_path(r'^todos/(\d+)/owner/$',views.owner_detail,name="owner_detail"),
    path('home/',views.home, name ="home")
]
