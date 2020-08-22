from django.urls import path
from . import views

app_name = 'www'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('subscribe/<int:video_id>', views.set_subscribe, name='subscribe'),
    path('unsubscribe/<int:video_id>', views.set_unsubscribe, name='unsubscribe'),
    path('channel/<int:channel_user_id>', views.channel_view, name='channel'),
    path('subscription/', views.subscriptions_view, name='subscription'),
    path('trending/', views.trending_video_list, name='trending')
]