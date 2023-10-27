from django.urls import path
from . import views

urlpatterns = [
    path('create/complaint/', views.ComplaintView.as_view())


]