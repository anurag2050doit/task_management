from django.urls import path

from api import views

urlpatterns = [
    path('tasks/', views.TasksAllAPI.as_view(), name='all-task'),
    path('categories/', views.CategoriesAllAPI.as_view(), name='all-categories'),
    path('tags/', views.TagsAllAPI.as_view(), name='all-tags'),
    path('task/<int:pk>/', views.TaskSingleAPI.as_view(), name='task-detail')
]
