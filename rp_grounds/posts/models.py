from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from timezone_field import TimeZoneField
from django.db.models.fields import PositiveIntegerField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from .dict import POST_TYPES, GENRE, GENDER_PREF, ROLE_TYPE, STYLES
# Create your models here.

def upload_location(instance, filename):
    return "{}/{}/{}".format("post",instance.user.username, filename)

class Post(models.Model):
    title = models.CharField(max_length=125)
    banner = models.ImageField(upload_to= upload_location, null=True, blank=True, width_field='max_height', height_field='max_width')
    max_height = PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(100),MinValueValidator(100)])
    max_width = PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(500),MinValueValidator(500)])
    content = models.TextField(null=True)
    private = models.BooleanField(default=False)
    publish = models.DateField(null=True, blank=True, auto_now_add=False, auto_now=False)
    timestamp = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    fandom = models.CharField(max_length=32)
    genre = models.CharField(choices=GENRE, default=GENRE[0][0], max_length=64)
    pref = models.CharField(choices=GENDER_PREF, default=GENDER_PREF[0][0], max_length=64)
    style = models.CharField(choices=STYLES, default="Select a Style", max_length=64)
    details = models.TextField(null=True, blank=True, max_length=64)
    rptype = models.CharField("Rating",choices=ROLE_TYPE, default='SFW', max_length=64)
    type = models.CharField(choices=POST_TYPES, null=True, blank=True, max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]