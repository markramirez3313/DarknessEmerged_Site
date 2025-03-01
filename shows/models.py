from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=75)
    show_location = models.CharField(max_length=75, default="TBD")
    show_date = models.DateField()
    doors_open = models.TimeField()
    flyer = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
