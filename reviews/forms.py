from django import forms

from .models import Review
from shops.models import Shop


class ReviewCreateForm(forms.Form):
    comment = forms.CharField(max_length=1000, widget=forms.Textarea)
    score = forms.IntegerField(widget=forms.HiddenInput)
    photo = forms.ImageField()
    shop = forms.ModelChoiceField(Shop.objects.all())
"""
class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'score', 'photo', 'shop',)
        widgets = {
            'score': forms.HiddenInput()
        }
"""
