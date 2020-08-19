from django.urls import path
from . import views

app_name = 'www'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('subscribe/<int:video_id>', views.subscribe_view, name='subscribe'),
    path('unsubscribe/<int:video_id>', views.unsubscribe_view, name='unsubscribe'),
]