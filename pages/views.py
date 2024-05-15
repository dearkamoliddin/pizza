from django.shortcuts import render
from django.views.generic import TemplateView

from pages.models import ScrollModel
from products.models import ProductModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pizza = ProductModel.objects.filter(category__name='Pizza')
        burgers = ProductModel.objects.filter(category__name='Burgers')
        salads = ProductModel.objects.filter(category__name='Salads')
        drinks = ProductModel.objects.filter(category__name='Drinks')
        fries = ProductModel.objects.filter(category__name='Fries')
        discount_products = ScrollModel.objects.all()[:5]
        contex = {
            'pizza': pizza,
            'burgers': burgers,
            'salads': salads,
            'drinks': drinks,
            'fries': fries,
            'discount_products': discount_products
        }
        return contex
