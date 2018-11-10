from django.urls import path
from .views import fbv,cbv,authenticate,generic_cbv

urlpatterns=[
    path('tasks/',fbv.task_list),
    path('task_detail/<int:pk>/',fbv.task_detail),
    path('ctasks/',cbv.TaskListView.as_view()),
    path('ctask_detail/<int:pk>/',cbv.TaskDetailView.as_view()),
    path('login/',authenticate.login),
    path('register/',authenticate.register),
    path('gtasks/',generic_cbv.TaskGenericListView.as_view())
]