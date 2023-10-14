from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

class user(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password1=models.CharField(max_length=255)

class log(models.Model):
    signins=models.BooleanField(default=False)
    username=models.CharField(max_length=255)
    emailid=models.EmailField()
