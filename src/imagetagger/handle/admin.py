from django.contrib import admin
from imagetagger.handle import models

class ScannedImageAdmin(admin.ModelAdmin):
    list_display = ('source', 'source_date', 'description', 'original')

admin.site.register(models.ScannedImage, ScannedImageAdmin)
admin.site.register(models.ImageFile, admin.ModelAdmin)
