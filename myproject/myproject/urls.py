from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('authorization/', include('authorization.urls')),
    path('posts/', include('posts.urls')),
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
]
