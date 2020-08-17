from django.contrib.auth.models import AbstractUser
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField


def user_profile_thumbnail_directory_path(instance, filename):
    return 'user_{}/profile/{}'.format(instance.username, 'thumbnail')


class User(AbstractUser):
    thumbnail = ProcessedImageField(
        upload_to=user_profile_thumbnail_directory_path,
        processors=[Thumbnail(50, 50)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60},
        null=True
    )  # 저장 옵션
