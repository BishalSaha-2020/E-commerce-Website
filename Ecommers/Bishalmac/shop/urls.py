from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/', views.about,name="AboutUs"),
path('tracker', views.tracker,name="TrackingStatus"),
path('search/', views.search,name="Search"),
path("prodView/<int:myid>", views.productView, name="ProductView"),
path('checkout/', views.checkout,name="Checkout"),
path('contact/', views.contact,name="contact"),

]