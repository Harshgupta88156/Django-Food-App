from django.contrib import admin
<<<<<<< HEAD
from .models import FoodItem  # Import your models here.
# Register your models here.
admin.site.register(FoodItem)  # Replace ... with your model names to register them in the admin site.
=======
from .models import Category, FoodItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'created_at')
    readonly_fields = ('created_at',)
>>>>>>> b58b87f (enhnaced features with CRUD operations)
