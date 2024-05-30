from django.contrib import admin
from .models import ImageModel

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']
# Register your models here.
