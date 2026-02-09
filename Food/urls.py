from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:food_id>/', views.foodId, name='foodId'),
    
=======
app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('food/<int:food_id>/', views.foodId, name='foodId'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
>>>>>>> b58b87f (enhnaced features with CRUD operations)
]
