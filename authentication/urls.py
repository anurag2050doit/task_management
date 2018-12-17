from django.urls import path

from authentication.views import LoginView, LogoutView, UserDetailView

urlpatterns = [
    path('username/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
