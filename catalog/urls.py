from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ProductDetailsView, ProductListView, ProductCreateView, contacts, ProductUpdateView, ProductDeleteView, UnpublishProductView, ProductCategoryListView


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product'),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("category_products/<int:pk>/", ProductCategoryListView.as_view(), name="category_products"),
]