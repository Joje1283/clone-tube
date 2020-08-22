from django.contrib.auth.models import AbstractUser, models
from django.urls import reverse
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

    @property
    def get_channel_url(self):
        return reverse("www:channel", args=[self.pk,])

    @property
    def subscribe_channels(self):
        """구독중인 유저객체 반환"""
        subscribing = json.loads(self.subscribing)
        return User.objects.filter(pk__in=subscribing)

    def is_subscribe(self, user):
        """user가 self.user에 대한 구독 여부 반환"""
        subscribing_by = json.loads(self.subscribing_by)
        return True if user.pk in subscribing_by else False

    def subscriber_count(self):
        """구독자 수 반환"""
        return len(json.loads(self.subscribing_by))

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
