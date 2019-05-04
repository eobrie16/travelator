from django.db import models
from datetime import date, timedelta
from django.urls import reverse

class Search(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    # dates
    today = date.today()
    tomorrow = today + timedelta(days=1)
    start_date = models.DateField(default=today)
    end_date = models.DateField(default=tomorrow)
    # for now let's make this a char field
    location = models.CharField(max_length=200)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("search_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.city
