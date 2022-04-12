from django.contrib import admin
from .models import Product,Stock, Order_request, Order_post, Store


admin.site.register(Product)
admin.site.register(Order_request)
admin.site.register(Order_post)
admin.site.register(Store)
admin.site.register(Stock)

