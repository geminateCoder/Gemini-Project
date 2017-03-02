from django import forms
from .models import Character
from timezone_field import TimeZoneFormField
from django.conf import settings
from django.views.generic import DeleteView


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('firstname', 'lastname', 'age', 'img', 'original')
        #if original then creator is creator else creator is rcreator

