from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ReviewCreateForm


class ReviewCreateView(FormView):
    form_class = ReviewCreateForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.save()
        return super().form_valid(form)
