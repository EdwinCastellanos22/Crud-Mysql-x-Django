from app1.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('cuenta/', include('django.contrib.auth.urls')),
]
