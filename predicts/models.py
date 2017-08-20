from django.db import models


# Create your models here.
class Predict(models.Model):
    title = models.TextField()
    rating = models.FloatField()

    # introduction = models.TextField()
    # area = models.CharField(max_length=15)
    # party_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title
