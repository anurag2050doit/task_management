from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^tasks/$', views.TasksAllAPI.as_view(), name='all-task'),
    url(r'^categories/$', views.CategoriesAllAPI.as_view(), name='all-categories'),
    url(r'tags/$', views.TagsAllAPI.as_view(), name='all-tags'),
    url(r'^task/(?P<pk>\d+)$', views.TaskSingleAPI.as_view(), name='task')
]
