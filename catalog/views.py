from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from django.views.generic import DetailView, ListView, TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо за обращение, {name}!")

    return render(request, template_name='catalog/home.html')


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product