from django.urls import path
from .views import change_language

urlpatterns = [
    path('change-language/', change_language, name='change_language'),
]
