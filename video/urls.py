from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    # path('test/', views.test, name='test'),
]