from django.db import models
<<<<<<< HEAD

# Create your models here.
class FoodItem(models.Model):
    itemName = models.CharField(max_length=100)
    itemDescription = models.CharField(max_length=250)  
    itemPrice = models.DecimalField(max_digits=6, decimal_places=2)
=======
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    description = models.TextField()

    def __str__(self): return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self): return f"Order {self.id} by {self.user.username}"
>>>>>>> b58b87f (enhnaced features with CRUD operations)
