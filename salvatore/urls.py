from django.contrib import admin
from django.urls import path, include
from webpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('salvatore/', include('webpage.urls')),
]
