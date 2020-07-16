from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance.user, filename)


class Video(models.Model):
    title = models.CharField(verbose_name='title', max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='description')
    upload = models.FileField(upload_to=user_directory_path)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
