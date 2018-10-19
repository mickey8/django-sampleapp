from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ShopCreateForm


class ShopCreateView(LoginRequiredMixin, CreateView):
    form_class = ShopCreateForm
    success_url = reverse_lazy('top')
    model = form_class.Meta.model
