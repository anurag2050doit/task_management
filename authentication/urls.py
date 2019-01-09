from django.urls import path, include

from authentication.views import LoginView, LogoutView, UserView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('username', UserView, basename='user')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('', include(router.urls)),
]
