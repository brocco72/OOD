from datetime import datetime
# from smart_selects.db_fields import ChainedForeignKey
from appdirs import unicode
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CITIES = (
    ('تهران', 'تهران'),
    ( 'اراک', 'اراک'),
    ('سنندج', 'سنندج'),
    ('یاسوج', 'یاسوج'),
    ('بوشهر', 'بوشهر'),
    ('جم', 'جم'),
    ('اصفهان', 'اصفهان'),
    ('تبریز', 'تبریز'),
    ('قزوین', 'قزوین'),
    ('مشهد', 'مشهد'),
    ('ساری', 'ساری'),
    ('بیرجند', 'بیرجند'),
    ('زاهدان', 'زاهدان'),
    ('کرمان', 'کرمان'),
    ('زابل', 'زابل'),
    ('اهواز', 'اهواز'),
    ('آبادان', 'آبادان'),
    ('قم', 'قم'),
    ('کرمانشاه', 'کرمانشاه'),
    ('ایلام', 'ایلام'),
    ('ساوه', 'ساوه'),
    ('قائن', 'قائن'),
    ('قوچان', 'قوچان'),
    ('یزد', 'یزد'),
    ('شیراز', 'شیراز'),
    ('رشت', 'رشت'),
    ('شهرکرد', 'شهرکرد'),
    ('طبس', 'طبس'),
    ('نیشابور', 'نیشابور'),
    ('ری', 'ری'),
    ('کرج', 'کرج'),
    ('سمنان', 'سمنان'),
    ('شاهرود', 'شاهرود'),
    ('سبزوار', 'سبزوار'),
)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITIES, blank=True)
    address = models.TextField()
    email = models.CharField(max_length=200)
    level = models.PositiveIntegerField(default=0)
    balance = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse(self, 'new-customer')


class Provider(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50, choices=CITIES, blank=True)

    def get_absolute_url(self):
        return reverse(self, 'new-provider')


class Product(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.0)
    off = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse(self, 'new-product')


class SellInvoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    total = models.FloatField(default=0.0)


class BuyInvoice(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    total = models.FloatField(default=0.0)


class SellInvoiceItems(models.Model):
    invoice = models.ForeignKey(SellInvoice, related_name='sell_invoice', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='sell_item_product', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    off = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)


class BuyInvoiceItems(models.Model):
    invoice = models.ForeignKey(BuyInvoice, related_name='buy_invoice', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='buy_item_product', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.0)


class CustomerLevelOff(models.Model):
    level = models.PositiveIntegerField(unique=True)
    off = models.FloatField(default=0.0)