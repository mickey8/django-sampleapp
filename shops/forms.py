from django import forms

from .models import Prefecture, Shop


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
