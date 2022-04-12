from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Stock, Store, Order_post, Order_request


class ProductSerializer(serializers.ModelSerializer):
    store_name = serializers.ReadOnlyField(source='store.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price',
                  'created_date', 'cost', 'store_name']


class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Stock
        fields = ['id', 'product_name', 'quantity', 'created_date',
                  'updated_date', 'received_quantity', 'payment', 'spoilt_quantity']


class OrderPostSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Order_post
        fields = ['id', 'product_name', 'quantity',
                  'created_date', 'updated_date']


class OrderRequestSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Order_request
        fields = ['id', 'product_name', 'quantity',
                  'created_date', 'updated_date']


class StoreSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Store
        fields = ['id', 'name', 'admin', 'clerk']
