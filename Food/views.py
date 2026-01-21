from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem
# Create your views here.


def index(request):
    food_item = FoodItem.objects.all()

    return HttpResponse(food_item)


# def hey(request):
#     return HttpResponse("Hello 2, welcome to the Food App!")