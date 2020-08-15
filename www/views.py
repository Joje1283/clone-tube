from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Video
from hitcount.views import HitCountDetailView


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {
        'videos': videos,
    })


# def video_detail(request, pk):
#     video = get_object_or_404(Video, pk=pk)
#     return render(request, 'video/video_detail.html', {
#         'video': video,
#     })


class VideoDetailView(HitCountDetailView):
    model = Video
    template_name = 'video/video_detail.html'
    count_hit = True


video_detail = VideoDetailView.as_view()
