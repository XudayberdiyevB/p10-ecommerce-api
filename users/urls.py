from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterView, CustomTokenObtainPairView, ProfileView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", ProfileView.as_view(), name="profile")
]
