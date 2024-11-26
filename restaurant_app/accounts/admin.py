# menu/admin.py
from django.contrib import admin
from menu.models import Category, Dish

admin.site.register(Category)
admin.site.register(Dish)

# orders/admin.py
from django.contrib import admin
from orders.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# reviews/admin.py
from django.contrib import admin
from reviews.models import Review

admin.site.register(Review)
