from django.db import models

# Create your models here.


class category(models.Model):
    name=models.CharField(default="",max_length=400)
    description=models.TextField(default="")
    def __str__(self):
        return self.name