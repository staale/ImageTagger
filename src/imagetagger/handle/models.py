from django.db import models

class ImageFile(models.Model):
    path = models.CharField(max_length=150)
    scanned_image = models.ForeignKey("ScannedImage", null=True)

    def __unicode__(self):
        if self.scanned_image:
            return "%s: %s"%(self.scanned_image.source, self.path)
        else:
            return "*Unhandled*: %s"%(self.path)

class ScannedImage(models.Model):
    original = models.OneToOneField(ImageFile)
    source = models.CharField(max_length=150)
    source_date = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=500)

class ImageTag(models.Model):
    scanned_image = models.ForeignKey(ScannedImage)
    tag = models.CharField(max_length=150, db_index=True)