from django.shortcuts import render


def home(request):
    return render(request, 'video/home.html')


def video_detail(request, pk):
    return render(request, 'video/video_detail.html')


def test(request):
    return render(request, 'video/video_detail2.html')