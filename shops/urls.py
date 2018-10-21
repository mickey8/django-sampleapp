from django.urls import path

from . import views

app_name = 'shops'
urlpatterns = [
    path('ranking/', views.ShopRankingView.as_view(), name='ranking'),
    path('create/', views.ShopCreateView.as_view(), name='create'),
]
