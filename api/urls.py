from django.contrib import admin
from django.urls import include, path
from api.mikao import views
from django.conf import settings
from django.conf.urls import url, include
from rest_framework_simplejwt import views as jwt_views
 
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    url('admin/', admin.site.urls),
    url('api/', include('api.mikao.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]