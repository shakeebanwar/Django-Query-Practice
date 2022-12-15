
from django.contrib import admin
from django.urls import path, include
from bookautherapp.views import *
from django.conf import settings
#for images
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
	path('', include('bookautherapp.urls')),
    path('bookautherapp/', include('bookautherapp.urls')),
    path('bookautherapp-auth/', include('rest_framework.urls')),
    path('bookautherapp/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('bookautherapp/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]