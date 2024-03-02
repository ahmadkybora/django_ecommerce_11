from django.urls import path
from .views import articles, articleById

urlpatterns = [
    path('', articles, name='articles'),
    path('<int:pk>/', articleById, name='articleById')
]