from django.db import models
from users.models import CustomUser
class Songs(models.Model):
    audio_file = models.FileField(upload_to="/uploads")
    song_image = models.FileField(upload_to="/uploads")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    song_length = models.IntegerField(null=True,blank=True)
    singer = models.ForeignKey(CustomUser,on_delete=models.SET_NULL)
    