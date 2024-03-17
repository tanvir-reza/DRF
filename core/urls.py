from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework_simplejwt.views import TokenVerifyView
from app.views import CustomTokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api-user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-user/token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
