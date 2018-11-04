from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView

from .forms import UserCreationForm


class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('top')
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user
