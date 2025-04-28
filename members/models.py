from django.db import models

# Create your models here.
class Member(models.Model):
    memberPhoto = models.ImageField(default = "", blank=True)
    name = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name
