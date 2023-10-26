from django.urls import path, re_path
from . import views

app_name = 'product'
urlpatterns = [
    path('type/add/', views.ProductTypeView.as_view(), name='product-type'),
    path('type/detail/<int:id>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),
    path('degree/add/', views.DegreeView.as_view(), name='degree'),
    path('degree/detail/<int:id>', views.DegreeDetailView.as_view(), name='degree-detail'),
    path('unit/add/', views.UnitView.as_view(), name='unit'),
    path('unit/detail/<int:id>', views.UnitDetailView.as_view(), name='unit-detail'),
    path('', views.ProductListView.as_view(), name='Product-list'),
    path('add/', views.ProductAddView.as_view(), name='product'),
    re_path(r'detail/(?P<slug>[^/]+)/?$', views.ProductDetailView.as_view(), name='product-detail'),
    path('price/', views.ProductPriceView.as_view(), name='product-price'),
    path('price/add/', views.ProductPriceAddView.as_view(), name='product-price-add'),
    path('price/<int:p_id>', views.EachProductPriceView.as_view(), name='product-price-history')
]
