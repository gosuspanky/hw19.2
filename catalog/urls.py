from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, category_products, product_description

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('<int:pk>/product/', product_description, name='product_description')
]
