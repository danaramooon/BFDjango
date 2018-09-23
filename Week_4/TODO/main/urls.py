from django.urls import path,re_path
from main import views

urlpatterns = [
    path('todos/', views.todos, name = "todos"),
    path('todos/1/completed/', views.completed_todos,name = "completed_todos"),
    re_path(r'^todos/([\w\_?]+)/order_by/$', views.todo_filter, name='order_by'),
    re_path(r'^todos/completed/([\w\_?]+)/order_by/$', views.completed_todo_filter, name='completed_order_by')
]
