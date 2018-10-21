from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    path('list/', views.ReviewListView.as_view(), name='list'),
]
