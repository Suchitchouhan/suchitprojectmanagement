from django.db import models
from categorymanagement.models import category

# Create your models here.
class product(models.Model):
    name=models.CharField(default="",max_length=1000)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='product',default='noimage.jpg', blank=True, null=True)
    def __str__(self):
        return self.name



        