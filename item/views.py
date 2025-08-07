from django.views.generic import ListView, TemplateView
from django.db.models import Count, Sum
from django.db import models
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Item, StockUpdate, Category
from .serializers import ItemSerializer, StockUpdateSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-updated_at')
    serializer_class = ItemSerializer

    @action(detail=False, methods=['get'], url_path='')
    def index(request):
        items = Item.objects.filter(is_sold=False)[0:6]
        categories = Category.objects.all()

        return render(request, 'core/index.html', {
            'categories': categories,
            'items': items,
        })
    

    @action(detail=False, methods=['get'], url_path='low-stock')
    def low_stock(self, request):
        """
        Return all products where quantity <= low_stock_threshold
        """
        low_stock_products = Item.objects.filter(quantity__lte=models.F('low_stock_threshold'))
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)

class StockUpdateViewSet(viewsets.ModelViewSet):
    queryset = StockUpdate.objects.all().order_by('-timestamp')
    serializer_class = StockUpdateSerializer
    

class ProductListView(ListView):
    model = Item
    template_name = 'item/product_list.html'
    context_object_name = 'products'
    paginate_by = 20  # optional

class LowStockListView(ListView):
    model = Item
    template_name = 'item/low_stock_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Item.objects.filter(quantity__lte=models.F('low_stock_threshold'))

class InventoryDashboardView(TemplateView):
    template_name = 'item/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_items = Item.objects.count()
        total_categories = Category.objects.count()
        low_stock_cout = Item.objects.filter(quantity__lte=models.F('low_stock_threshold')).count()

        total_stock_in = StockUpdate.objects.filter(quantity_change__gt=0).aggregate(total=Sum('quantity_change'))['total'] or 0
        total_stock_out = abs(StockUpdate.objects.filter(quantity_change__lt=0).aggregate(total=Sum('quantity_change'))['total'] or 0)

        top_categories = Category.objects.annotate(item_count=Count('items')).order_by('-item_count')[:5]

        context.update({
            'total_items': total_items,
            'total_categories': total_categories,
            'low_stock_count': low_stock_cout,
            'total_stock_in': total_stock_in,
            'total_stock_out': total_stock_out,
            'top_categories': top_categories,
        })
        return context

