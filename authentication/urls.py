from django.urls import path
from rest_framework import routers

from authentication.views import UserViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', UserViewSet)

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
]
