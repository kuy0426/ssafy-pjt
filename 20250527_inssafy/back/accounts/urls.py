from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info, name='user-info'),
    path('<int:pk>/', views.user_detail, name='user-detail'),
]