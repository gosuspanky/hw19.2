from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactPageView, ProductListView, ProductDetailView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='category_products'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product_description'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
