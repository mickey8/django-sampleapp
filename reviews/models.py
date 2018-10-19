from django.contrib.auth import get_user_model
from django.db import models

from shops.models import Shop

UserModel = get_user_model()


class Review(models.Model):
    comment = models.CharField(max_length=1000)
    photo = models.ImageField(blank=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
