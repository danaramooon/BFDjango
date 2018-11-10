from django.urls import path
from . import views

urlpatterns=[
    path('tasks/',views.task_list),
    path('task_detail/<int:pk>/',views.task_detail)
]