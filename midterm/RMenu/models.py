from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Restau(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    telephone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="restaurants")

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    restaurant = models.ForeignKey(Restau, on_delete=models.CASCADE, related_name="dishes", default=Restau)

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now())

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restau, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now())

class DishReview(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE,related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now())


