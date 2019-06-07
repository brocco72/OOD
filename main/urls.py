from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/new', CustomerCreateView.as_view(), name="new-customer"),
    path('provider/new', ProviderCreateView.as_view(), name="new-provider"),
    path('product/new', ProductCreateView.as_view(), name="new-product"),
    path('invoice/sale', views.sell_invoice_create, name="new-sale"),
    path('invoice/buy', views.buy_invoice_create, name="new-buy"),
    path('clear/sell', views.clear_sell, name="clear-sell"),
    path('clear/buy', views.clear_buy, name="clear-buy"),
    path('off/customer', views.level_off, name="customer-off"),
    path('off/product', views.product_off, name="product-off"),
    path('product/price', views.product_price, name="product-price"),
    path('product/list', views.product_list, name="product-list"),
    path('reports/gainloss', views.gain_loss, name="gain-loss"),
    path('reports/customer/stat', views.customer_stat, name="customer-stat")
    # path('result', HouseListView.as_view() , name="house-list"),
    # path('home-register', HouseCreateView.as_view(), name="home-register"),
    # path('about', views.about, name="about"),
    # path('home-detail/<int:pk>/', HouseDetailView.as_view(), name="home-detail"),
    # path('staty', views.staty, name="staty"),
    # path('rent/<int:pk>/', views.rent, name="home-rent"),
    # path('pay/<int:pk>', views.pay, name="pay"),
    # path('rent-success/', views.rent_success, name="rent-success"),
    # path('search/', views.search, name="search"),
]

