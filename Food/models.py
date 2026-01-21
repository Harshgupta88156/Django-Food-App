from django.db import models

# Create your models here.
class FoodItem(models.Model):
    itemName = models.CharField(max_length=100)
    itemDescription = models.CharField(max_length=250)  
    itemPrice = models.DecimalField(max_digits=6, decimal_places=2)