from django import forms
from .models import Post
from django.core.files.images import get_image_dimensions

class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content"
        ]

class PromptPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "banner",
            "title",
            "content"
        ]


class FanficPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content"
        ]
