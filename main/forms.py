from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.forms.models import inlineformset_factory
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout import Formset



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'family_name', 'city', 'address', 'email', 'level']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام"
        self.fields['family_name'].label = "نام خانوادگی"
        self.fields['city'].label = "شهر"
        self.fields['address'].label = "آدرس"
        self.fields['email'].label = "ایمیل"
        self.fields['level'].label =  "سطح تخفیف"


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'brand', 'city', 'address']

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام"
        self.fields['brand'].label = "برند"
        self.fields['city'].label = "شهر"
        self.fields['address'].label = "آدرس"


class ProviderModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ProductForm(ModelForm):
    provider = ProviderModelChoiceField(queryset=Provider.objects.all(), required=False)

    class Meta:
        model = Product
        fields = ['name', 'provider', 'number', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام"
        self.fields['provider'].label = "تامین کننده"
        self.fields['number'].label = "تعداد"
        self.fields['price'].label = "قیمت"


class SellInvoiceItemsForm(ModelForm):

    class Meta:
        model = SellInvoiceItems
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(SellInvoiceItemsForm, self).__init__(*args, **kwargs)
        self.fields['product'].label = "کالا"
        self.fields['number'].label = "تعداد"
        self.fields['price'].label = "قیمت"


class SellInvoiceForm(forms.ModelForm):

    class Meta:
        model = SellInvoice
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(SellInvoiceForm, self).__init__(*args, **kwargs)
        self.fields['customer'].label = "مشتری"
        self.fields['date'].label = "تاریخ"


class BuyInvoiceForm(forms.ModelForm):

    class Meta:
        model = BuyInvoice
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(BuyInvoiceForm, self).__init__(*args, **kwargs)
        self.fields['provider'].label = "تامین کننده"
        self.fields['date'].label = "تاریخ"


class SellInvoiceClearingForm(forms.Form):
    invoiceID = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(SellInvoiceClearingForm, self).__init__(*args, **kwargs)
        self.fields['invoiceID'].label = "شماره فاکتور"


class BuyInvoiceClearingForm(forms.Form):
    invoiceID = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(BuyInvoiceClearingForm, self).__init__(*args, **kwargs)
        self.fields['invoiceID'].label = "شماره فاکتور"


class ProductOffForm(forms.Form):

    productID = forms.IntegerField()
    off = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(ProductOffForm, self).__init__(*args, **kwargs)
        self.fields['productID'].label = "شماره محصول"
        self.fields['off'].label = " درصد تخفیف"


class CustomerLevelOffForm(forms.ModelForm):

    class Meta:
        model = CustomerLevelOff
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(CustomerLevelOffForm, self).__init__(*args, **kwargs)
        self.fields['level'].label = " سطح مشتری"
        self.fields['off'].label = " مبلغ تخفیف"
