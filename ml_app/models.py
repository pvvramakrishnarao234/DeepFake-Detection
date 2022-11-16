from django.db import models

# Create your models here.
class Item(models.Model):
    video_file_name = models.CharField(max_length=500)
    video_frames_name = models.CharField(max_length=500)
    video_cropped_name = models.CharField(max_length=500)
