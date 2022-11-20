from django.db import models

from categories.models import SuperCategory

# Create your models here.


class Subscription(models.Model):
    super_category = models.ForeignKey(
        to=SuperCategory, on_delete=models.PROTECT)
    subscription_name = models.CharField(max_length=254)
    subscription_price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.subscription_name
