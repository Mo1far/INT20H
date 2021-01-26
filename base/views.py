from collections import namedtuple

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from base.parsing import get_products


class ProductListView(ListView):
    template_name = 'base/product_list.html'
    context_object_name = 'products_list'
    ProductInfo = namedtuple('ProductInfo', ['title', 'cost', 'link'])

    def get_queryset(self):
        products = get_products()

        return [self.ProductInfo(product['title'],
                                 product['price'],
                                 product['link']) for product in sorted(products, key=lambda k: float(k['price']))]
