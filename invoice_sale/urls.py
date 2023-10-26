from django.urls import path
from . import views

app_name = 'invoice_sale'

urlpatterns = [
    path('add/', views.InvoiceSalesAddView.as_view(), name='add'),
    path('add/item/', views.InvoiceSalesItemAddView.as_view(), name='add-item'),
]
