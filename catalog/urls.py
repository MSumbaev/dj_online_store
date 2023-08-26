from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, CategoryCreateView, CategoryListView, ProductsListView, \
    CategoryUpdateView, CategoryDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    # path('products/<int:pk>', product, name='product'),
    path('category/<int:pk>', ProductsListView.as_view(), name='category'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/view/<int:pk>', ProductDetailView.as_view(), name='product_detail_view'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

]
