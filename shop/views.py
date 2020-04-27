from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin, View

from .models import Category, Product
from django.views.generic.list import ListView


class ProductContentListView(TemplateResponseMixin, View):
    """ Klasa odpowiedzialna za wyświetlenie wszystkich produktów """
    template_name = 'shop/products/list.html'

    def get(self, request, name_category=None):
        category = Category.objects.all()
        products = Product.objects.all()
        if name_category:
            products = Product.objects.filter(category=name_category)
        return self.render_to_response({'products': products,
                                        'category': category})


class ProductDetailListView(TemplateResponseMixin,View):
    template_name = 'shop/products/product/detail.html'

    def get(self, request, id_product):
        product = get_object_or_404(Product,id=id_product)
        return self.render_to_response({'product': product})