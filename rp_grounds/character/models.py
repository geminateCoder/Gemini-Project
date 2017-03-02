from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.


def upload_location(instance, filename):
    return "{}/{}/{}".format("characters", instance.username, filename)


class Character(models.Model):
    username = models.ForeignKey(
        User, default=1)
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24, null=True, blank=True)
    age = models.IntegerField(validators=[MaxValueValidator(9999, "No way can they be that old!")])
    img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    original = models.BooleanField(default=True)
    creator = models.CharField(max_length=32,null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstname + " " + self.lastname


    def get_absolute_url(self):
        return "character/%s/" % (self.id)



