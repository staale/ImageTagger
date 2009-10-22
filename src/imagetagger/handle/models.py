from django.db import models
import datetime

class ImageFile(models.Model):
    path = models.CharField(max_length=150)
    scan_date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.path

class ScannedImage(models.Model):
    original = models.OneToOneField(ImageFile)
    source = models.CharField(max_length=150)
    source_date = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=500)

class ImageTag(models.Model):
    scanned_image = models.ForeignKey(ScannedImage)
    tag = models.CharField(max_length=150, db_index=True)