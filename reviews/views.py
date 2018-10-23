from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .forms import ReviewCreateForm
from .models import Review


class ReviewListView(ListView):
    model = Review

    def get_queryset(self):
        return self.model.list_latest()


class ReviewCreateView(FormView):
    form_class = ReviewCreateForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.save()
        return super().form_valid(form)
