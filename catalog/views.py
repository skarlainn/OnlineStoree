from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy


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
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")