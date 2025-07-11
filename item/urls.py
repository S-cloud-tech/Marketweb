from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ItemViewSet)
router.register(r'stock-updates', StockUpdateViewSet)

app_name = 'item'

urlpatterns = [
    path('api/', include(router.urls)),
    path('products/', ProductListView.as_view(), name='low_stock_list'),
    path('products/low-stock/', LowStockListView.as_view(), name='low_stock_list'),
    path('dashboard/', InventoryDashboardView.as_view(), name='dashboard')
]
