from django import forms
from .models import UserProfile
from timezone_field import TimeZoneFormField
from django.conf import settings

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('displayname', 'img','timezone')