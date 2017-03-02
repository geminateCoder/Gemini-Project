from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from timezone_field import TimeZoneField
from django.utils import timezone
from datetime import datetime

# Create your models here.


def upload_location(instance, filename):
    return "{}/{}/{}".format("users",instance.user.username, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True)
    displayname = models.CharField(max_length=25)
    img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    timezone = TimeZoneField(default=timezone.now)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])