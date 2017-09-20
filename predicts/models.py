from django.db import models


# Create your models here.
class Predict(models.Model):
    title = models.CharField(max_length=128)
    release_day = models.DateField(default=0)
    naver_url = models.TextField()
    image_url = models.TextField()
    video_url = models.TextField()
    reserve_url = models.TextField()
    news_url = models.TextField()
    screen_num_7 = models.IntegerField(default=0)
    show_num_7 = models.IntegerField(default=0)
    money_num_7 = models.IntegerField(default=0)
    audience_num_7 = models.IntegerField(default=0)
    director_effect = models.IntegerField(default=0)
    distributor_effect = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    nationality = models.IntegerField(default=0)
    before_grade = models.FloatField()
    after_grade = models.FloatField()
    age = models.IntegerField(default=0)
    actor_effect = models.IntegerField(default=0)
    audience_class = models.IntegerField(default=0)
    audience_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title
