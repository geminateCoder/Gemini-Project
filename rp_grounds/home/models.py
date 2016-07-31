from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Goal(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField()

    def __str__(self):
        return self.title


def upload_location(instance, filename):
    return "{}/{}".format(instance.username, filename)


class Feature(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    staff = models.ForeignKey(User)
    img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    title = models.CharField(max_length=100)
    about = models.TextField()
    joined_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
