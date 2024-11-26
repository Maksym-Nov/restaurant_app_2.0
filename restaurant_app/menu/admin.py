# menu/admin.py
from django.contrib import admin
from .models import Category, Dish



# orders/admin.py
from django.contrib import admin
from orders.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# reviews/admin.py
from django.contrib import admin
from .models import Review

admin.site.register(Review)
