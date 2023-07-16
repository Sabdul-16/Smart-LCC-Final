from django.urls import path
from .views import home
from .admin import admin


urlpatterns = [
    path('', home, name='home'),
]
