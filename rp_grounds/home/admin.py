from django.contrib import admin

# Register your models here.
from .models import NewsPost, Goal, Feature, StaffList

admin.site.register(NewsPost)
admin.site.register(Goal)
admin.site.register(Feature)
admin.site.register(StaffList)
