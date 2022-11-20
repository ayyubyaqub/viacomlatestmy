from django.db import models
from categories.models import *

# Create your models here.
# class Work(models.Model):
#     super_category = models.ForeignKey(to=SuperCategory, on_delete=models.PROTECT)
#     company_name = models.CharField(max_length=254)
#     video_name = models.CharField(max_length=254)
#     video_link = models.CharField(max_length=254)
#     thumbnail = models.ImageField()

#     def __str__(self):
#         return self.video_name