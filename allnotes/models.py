

# Create your models here.
from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    license_end_date = models.DateField()

    def __str__(self):
        return self.name