from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from hitcount.models import HitCount

from .forms import ReplyForm
from .models import Video
from hitcount.views import HitCountDetailView
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    videos = Video.objects.all()
    s = request.GET.get('s')
    if s:
        videos = videos.filter(title__icontains=s)
    return render(request, 'home.html', {
        'videos': videos,
        'search': s,
    })


class VideoDetailView(HitCountDetailView):
    model = Video
    template_name = 'video/video_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_form'] = ReplyForm()
        return context


video_detail = VideoDetailView.as_view()


def set_subscribe(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    creater = get_object_or_404(User, pk=video.user.pk)
    subscriber = request.user
    subscriber.subscribe(creater)
    return redirect(reverse('www:video_detail', args=[video_id]))


def set_unsubscribe(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    creater = get_object_or_404(User, pk=video.user.pk)
    subscriber = request.user
    subscriber.unsubscribe(creater)
    return redirect(reverse('www:video_detail', args=[video_id]))


def channel_view(request, channel_user_id):
    videos = Video.objects.filter(user_id=channel_user_id)
    return render(request, 'home.html', {
        'videos': videos,
    })


def subscriptions_view(request):
    user = request.user
    users = user.subscribe_channels
    videos = Video.objects.filter(user__in=users)
    return render(request, 'home.html', {
        'videos': videos,
    })


def trending_video_list(request):
    hit_count_list = HitCount.objects.order_by('hits').values_list('object_pk', flat=True)
    videos = []
    for hit_count in hit_count_list:
        videos.append(get_object_or_404(Video, pk=hit_count))
    return render(request, 'home.html', {
        'videos': videos,
    })
