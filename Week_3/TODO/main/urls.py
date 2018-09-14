from django.urls import path
from main import views

urlpatterns=[
    path('', views.tasks),
    path('1/completed/', views.completed_tasks),
]