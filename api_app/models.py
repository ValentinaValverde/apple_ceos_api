from django.db import models

# Create your models here.
class AppleCeo(models.Model):
    name = models.TextField(max_length=100)
    slug = models.TextField(max_length=100)
    first_year_active = models.IntegerField()

    def __str__(self):
        return self.name
    