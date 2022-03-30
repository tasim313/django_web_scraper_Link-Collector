from django.urls import path
from .views import *

urlpatterns = [
    path('', scrape, name='scrape'),
    path('delete/', clear, name='delete'),
]