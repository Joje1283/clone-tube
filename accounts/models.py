from django.contrib.auth.models import AbstractUser, models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField
import json


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
    subscribing = models.CharField(max_length=5000, default='[]')
    subscribing_by = models.CharField(max_length=5000, default='[]')

    def subscribe(self, user):
        subscribing = json.loads(self.subscribing)
        if not user.pk in subscribing and not self.pk in json.loads(user.subscribing_by):
            user.subscribed(self)
            subscribing = json.loads(self.subscribing)
            subscribing.append(user.pk)
            self.subscribing = json.dumps(subscribing)
            self.save()

    def subscribed(self, user):
        if not user.pk in json.loads(self.subscribing_by):
            subscribing_by = json.loads(self.subscribing_by)
            subscribing_by.append(user.pk)
            self.subscribing_by = json.dumps(subscribing_by)
            self.save()

    def unsubscribe(self, user):
        subscribing = json.loads(self.subscribing)
        if user.pk in subscribing and self.pk in json.loads(user.subscribing_by):
            user.unsubscribed(self)

            if user.pk in subscribing:
                subscribing.remove(user.pk)
            self.subscribing = json.dumps(subscribing)
            self.save()

    def unsubscribed(self, user):
        subscribing_by = json.loads(self.subscribing_by)
        if user.pk in subscribing_by:
            if user.pk in subscribing_by:
                subscribing_by.remove(user.pk)
            self.subscribing_by = json.dumps(subscribing_by)
            self.save()
