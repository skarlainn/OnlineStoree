from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products_list, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', products_list, name='products_list'),
    path('product/<int:pk>/', product_details, name='product')
]