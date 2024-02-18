from django.urls import path
from . import views as users_views

urlpatterns = [
    path("", users_views.register, name='user-login')
]