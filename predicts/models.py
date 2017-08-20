from django.db import models


# Create your models here.
class Predict(models.Model):
    title = models.CharField(max_length=128)
    rating = models.FloatField()
    distributor = models.IntegerField(default=0)
    num_viewers = models.IntegerField(default=0)

    def __str__(self):
        return self.title
