from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lp.urls')),  # Include URLs from the lp app
    # path('accounts/', include('django.contrib.auth.urls')),  # Remove this line
]
