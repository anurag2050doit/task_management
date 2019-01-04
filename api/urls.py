from django.urls import path, include

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.CategoryView)
router.register('tag', views.TagView)
router.register('task', views.TaskView)


urlpatterns = [
    path('', include(router.urls)),
]


#
# urlpatterns = [
#     path('tasks/', views.TasksAllAPI.as_view(), name='all-task'),
#     path('categories/', views.CategoriesAllAPI.as_view(), name='all-categories'),
#     path('tags/', views.TagsAllAPI.as_view(), name='all-tags'),
#     path('task/<int:pk>/', views.TaskSingleAPI.as_view(), name='task-detail'),
#     path('task/add/', views.TaskCreateAPI.as_view(), name='task-create'),
# ]
