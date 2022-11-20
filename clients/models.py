from django.db import models

from categories.models import SuperCategory

# Create your models here.


class Clients(models.Model):
    serial_number=models.IntegerField(null=True,blank=True)
    super_category = models.ForeignKey(
        to=SuperCategory, on_delete=models.PROTECT,related_name='client')
    client_name = models.CharField(max_length=254)
    client_logo = models.ImageField()
    client_cover = models.ImageField()
    client_videos = models.IntegerField()
    client_shoots = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.client_name


class ClientVideos(models.Model):
    client = models.ForeignKey(to=Clients, on_delete=models.CASCADE)
    video = models.FileField()

    def __str__(self):
        return self.client
