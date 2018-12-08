from django import forms

from .models import Prefecture, Shop


class ShopCreateForm(forms.Form):
    name = forms.CharField(max_length=128, label='名称')
    kana_name = forms.CharField(max_length=255, label='カナ名称')
    phone_number = forms.CharField(max_length=10, label='電話番号')
    prefecture = forms.ModelChoiceField(Prefecture.objects.all(), label='都道府県')
    address = forms.CharField(max_length=255, label='住所')
