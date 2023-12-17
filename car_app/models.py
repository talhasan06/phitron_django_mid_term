from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    headquarters = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    
    def __str__(self):
        return self.brand_name
    
class Car(models.Model):
    model_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    year = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/',blank=True, null = True)

    def __str__(self):
        return f"{self.model_name}"

class Comment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.model_name}"