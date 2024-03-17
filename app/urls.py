from django.urls import path
from . import views
urlpatterns = [
    path('',views.apiOverView, name='overview'),
    path('tasks/',views.taskList, name='task-list'),
    path('task-detail/<str:pk>/',views.taskDetail, name='task-details'),
    path('task-create/',views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/',views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/',views.taskDelete, name='task-delete'),
    path('myview/',views.myview, name='myview'),
]
