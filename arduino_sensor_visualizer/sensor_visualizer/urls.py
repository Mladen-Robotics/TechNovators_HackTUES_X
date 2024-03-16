from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('',include('read_data.urls')),
    path('admin/', admin.site.urls)
]
