from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('travel/', views.hello_visitor, name='hello_visitor'),
    path('travel/new/', views.CreateSearchView.as_view(), name='search'),
    path('travel/<pk>/', views.SearchDetailView.as_view(), name='search_detail'),
]