from django import views
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('stocks', views.StockViewSet)
router.register('stores', views.StoreViewSet)
router.register('order_posts', views.OrderPostViewSet)
router.register('order_requests', views.OrderRequestViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),

    


]