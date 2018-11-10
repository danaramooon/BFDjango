from django.urls import path,re_path
from main import views

urlpatterns = [
    path('todos/', views.TaskListView.as_view(), name='todos'),
    path('todos/completed/', views.CompleteListView.as_view(),name = "completed_todos"),
    path('todos/create/', views.TaskCreateView.as_view(), name='new_add'),
    path('todos/<int:pk>/delete/',views.TaskDeleteView.as_view(),name="delete"),
    path('todos/<int:pk>/update/',views.TaskUpdateView.as_view(),name = "update"),
    path('home/',views.home, name ="home")
]
