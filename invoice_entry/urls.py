from django.urls import path

from . import views

app_name = 'InvoiceEntry'
urlpatterns = [
    path('add/', views.InvoiceEntryAddView.as_view(),
         name='add'),
    path('item/add/', views.InvoiceEntryItemAddView.as_view(),
         name='item-add'),
    path('show/all/', views.InvoiceEntryShowAllView.as_view(),
         name='show all'),
    path('show/detail/<int:pk>/', views.InvoiceEntryShowDetailView.as_view(),
         name='show-detail'),
    path('show/detail/wholesaler/<int:wholesaler_id>/', views.InvoiceEntryShowDetailWholesaler.as_view(),
         name='detail-wholesaler')
]
