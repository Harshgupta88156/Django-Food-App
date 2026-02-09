<<<<<<< HEAD
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
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodItem, Category, Order
import json


def index(request):
    """Main menu page displaying all food items"""
    query = request.GET.get('q', '')
    
    if query:
        items = FoodItem.objects.filter(name__icontains=query)
    else:
        items = FoodItem.objects.all()
    
    categories = Category.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'query': query
    }
    return render(request, 'menu.html', context)


def foodId(request, food_id):
    """Detail view for a specific food item"""
    food_item = get_object_or_404(FoodItem, id=food_id)
    
    context = {
        'food_item': food_item
    }
    return render(request, 'food_detail.html', context)


@login_required
def checkout(request):
    """Checkout page for processing orders"""
    if request.method == 'POST':
        cart_data = request.POST.get('cart_data')
        
        if cart_data:
            try:
                cart_items = json.loads(cart_data)
                
                if cart_items:
                    # Calculate total price
                    total_price = sum(float(item['price']) for item in cart_items)
                    
                    # Create order
                    order = Order.objects.create(
                        user=request.user,
                        total_price=total_price
                    )
                    
                    messages.success(request, f'Order #{order.id} placed successfully!')
                    return redirect('order_success', order_id=order.id)
                else:
                    messages.error(request, 'Your cart is empty.')
            except json.JSONDecodeError:
                messages.error(request, 'Invalid cart data.')
        else:
            messages.error(request, 'No cart data received.')
    
    return render(request, 'checkout.html')


def order_success(request, order_id):
    """Order confirmation page"""
    order = get_object_or_404(Order, id=order_id)
    
    context = {
        'order': order
    }
    return render(request, 'order_success.html', context)


def menu_view(request):
    """Alternative menu view (alias for index)"""
    return index(request)
>>>>>>> b58b87f (enhnaced features with CRUD operations)
