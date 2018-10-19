from django.urls import path

from . import views

app_name = 'shops'
urlpatterns = [
    path('create/', views.ShopCreateView.as_view(), name='create'),
]
