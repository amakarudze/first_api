from django.urls import path

from .views import product_list, product_detail,manufacturer_list, manufacturer_detail
# from .views import ProductDetailView, ProductListView


urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('manufacturers/', manufacturer_list, name='manufacturers'),
    path('manufacturer/<int:pk>/', manufacturer_detail, name='manufacturer'),
    # path('', ProductListView.as_view(), name='product_list'),
    # path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
