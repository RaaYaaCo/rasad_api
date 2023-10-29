from django.urls import path
from . import views

urlpatterns = [
    path('create/complaint/', views.CreateComplaintView.as_view())


]