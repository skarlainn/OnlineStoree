from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import ProductForm, ProductModeratorForm
from .models import Product
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Category
from .services import get_products_list_by_category


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm


class ProductDeleteView(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    permission_required = 'catalog.delete_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if request.user == product.owner or request.user.has_perm("catalog.delete_product"):
            product.delete()
            return redirect(reverse("catalog:home"))
        else:
            return HttpResponseForbidden("У Вас нет прав на удаление продукта!")


class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас недостаточно прав для снятия продукта с публикации")
        product.is_published = False
        product.save()
        return redirect('catalog:product', pk=product.id)

class ProductCategoryListView(ListView):
    model = Category
    template_name = 'catalog/products_list_by_category.html'
    context_object_name = 'category'

    def get_queryset(self, *args, **kwargs):
        queryset = get_products_list_by_category(self.kwargs.get('pk'))

        return queryset
