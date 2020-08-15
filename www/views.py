from django.shortcuts import render, get_object_or_404
from .models import Video


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {
        'videos': videos,
    })


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/video_detail.html', {
        'video': video,
    })
