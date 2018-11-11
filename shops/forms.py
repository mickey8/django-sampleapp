from django import forms

from .models import Prefecture, Shop


class ShopCreateForm(forms.Form):
    name = forms.CharField(max_length=128)
    kana_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=10)
    prefecture = forms.ModelChoiceField(Prefecture.objects.all())
    address = forms.CharField(max_length=255)


class ShopCreateForm2(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
