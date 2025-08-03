from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('auth/', include('users.urls')),

    # spectacular schema + swagger + redoc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Токен для входа
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Обновление токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
