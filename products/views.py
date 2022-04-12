
from rest_framework.response import Response
from .serializers import ProductSerializer, StockSerializer, OrderPostSerializer, OrderRequestSerializer, StoreSerializer
from rest_framework import viewsets
from .models import Product, Stock, Store, Order_post, Order_request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    
 
class OrderPostViewSet(viewsets.ModelViewSet):
    queryset = Order_post.objects.all()
    serializer_class = OrderPostSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class OrderRequestViewSet(viewsets.ModelViewSet):
    queryset = Order_request.objects.all()
    serializer_class = OrderRequestSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
