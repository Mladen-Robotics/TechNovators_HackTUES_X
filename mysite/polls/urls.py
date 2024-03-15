from django.urls import path
from .views import  chatbot_view
from . import views

urlpatterns = [
    path("math", views.math_AI, name="math"),
    path("ip", views.IP_AI, name="ip"),
    path("general", views.general_AI, name="general"),
    path("", views.index, name="index"),
    path('chatbot/', chatbot_view, name='chatbot_view'),    
]