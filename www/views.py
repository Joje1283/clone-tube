from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video
from hitcount.views import HitCountDetailView
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {
        'videos': videos,
    })


class VideoDetailView(HitCountDetailView):
    model = Video
    template_name = 'video/video_detail.html'
    count_hit = True


video_detail = VideoDetailView.as_view()


def subscribe_view(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    creater = get_object_or_404(User, pk=video.user.pk)
    subscriber = request.user
    subscriber.subscribe(creater)
    return redirect(reverse('www:video_detail', args=[video_id]))


def unsubscribe_view(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    creater = get_object_or_404(User, pk=video.user.pk)
    subscriber = request.user
    subscriber.unsubscribe(creater)
    return redirect(reverse('www:video_detail', args=[video_id]))
