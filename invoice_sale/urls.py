from django.urls import path
from . import views

app_name = 'invoice_sale'

urlpatterns = [
    path('add/', views.InvoiceSalesAddView.as_view(), name='add'),
    path('add/item/', views.InvoiceSalesItemAddView.as_view(), name='add-item'),
    path('show/all/', views.InvoiceSalesShowAllView.as_view(), name='show-all'),
    path('show/detail/<int:pk>/', views.InvoiceSalesShowDetailView.as_view(), name='show-detail'),
    path('show/detail/wholesaler/<int:wholesaler_ugo_id>/', views.InvoiceSalesShowDetailWholesalerView.as_view(),
         name='detail-wholesaler'),
    path('show/detail/store/<int:store_ugo_id>/', views.InvoiceSalesShowDetailStoreView.as_view(), name='detail-store')
]
