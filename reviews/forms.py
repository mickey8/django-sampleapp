from django import forms

from .models import Review
from shops.models import Shop


class ReviewCreateForm(forms.Form):
    """口コミ投稿画面のフォーム"""
    shop = forms.ModelChoiceField(Shop.objects.all(), label='お店')
    comment = forms.CharField(max_length=1000, widget=forms.Textarea, label='コメント')
    score = forms.IntegerField(widget=forms.HiddenInput)
    photo = forms.ImageField(label='写真')
