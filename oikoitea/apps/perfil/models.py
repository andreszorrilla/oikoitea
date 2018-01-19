from django.db import models

from django.contrib.auth.models import User
from django.conf import settings


def user_directory_path(instance, filename):
    return 'profiles/user_{0}/{1}'.format(instance.user.id, filename)

default_profile_pic = settings.MEDIA_URL + 'profiles/default.png'

class UserProfile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    address     = models.CharField(max_length=20, default="")
    avatar      = models.ImageField(upload_to=user_directory_path, blank=True)

    def avatar_url(self):
        try:
            if self.avatar and hasattr(self.avatar, 'url'):
                return self.avatar.url
        except(ValueError):
            return default_profile_pic
        return default_profile_pic

    def __unicode__(self):
        return unicode(self.some_field) or u''
