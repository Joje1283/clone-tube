from django.forms import ModelForm
from .models import Reply


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
