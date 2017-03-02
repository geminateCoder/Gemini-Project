from django.contrib import admin
from .models import Character
# Register your models here.

class CharaModelAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "username", "created_on"]
    #list_display_links = ["updated"]
    #list_editable = ["title"]
    #list_filter = ["updated","timestamp"]
    search_fields = ["firstname", "lastname", "username"]
    class Meta:
        model = Character


admin.site.register(Character, CharaModelAdmin)
