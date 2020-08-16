from django.utils import timezone
from django.db import models
from django.conf import settings
from datetime import timedelta
from hitcount.models import HitCountMixin


def user_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance.user, 'video')


def user_thumbnail_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance.user, 'thumbnai')


class Video(models.Model, HitCountMixin):
    title = models.CharField(verbose_name='title', max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='description')
    upload = models.FileField(upload_to=user_directory_path)
    thumbnail = models.ImageField(upload_to=user_thumbnail_directory_path, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def created(self):
        delta = timezone.now() - self.created_at
        if delta < timedelta(days=1):
            return f'{int(delta.total_seconds() // 60 // 60)}시간 전'
        else:
            return f'{delta.days}일 전'

