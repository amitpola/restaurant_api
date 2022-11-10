from django.db import models

# Create your models here.

#model for restaurants with various attributes
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=30,choices=(
        ("Vegetaian", "Veg"),("Non Vegetarian","Non Veg"),
    ))
    rating = models.IntegerField()
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


