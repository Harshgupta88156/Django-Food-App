from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem
from django.template import loader
# Create your views here.


def index(request):
    food_item = FoodItem.objects.all()
    template = loader.get_template('Food/index.html')
    context = {
        'food_item': food_item
    }
    return HttpResponse(template.render(context, request))


def foodId(request, food_id):

    food_description = FoodItem.objects.get(id=food_id)
    resp = str(food_id) + " " + food_description.itemDescription
    return HttpResponse(resp)