from django.conf.urls import url

from api import views

# urlpatterns = [
#     url(r'tickets', views.TaskAllAPI.as_view(), name='all_task'),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#
# ]

urlpatterns = [
    url(r'^task', views.TaskAllAPI.as_view(), name='task'),
]
