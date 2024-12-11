from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField(Category)
    stock = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    brand = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    thumbnail = models.URLField()


    def __str__(self):
        return self.title