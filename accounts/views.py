from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Create your views here.

class ProfileView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user
