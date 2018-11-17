from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import UserCreationForm, UserChangeForm


class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('top')
        return super().dispatch(request, *args, **kwargs)


class UserChangeView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'accounts/user_change.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def get_object(self):
        return self.request.user


class ProfileView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user
