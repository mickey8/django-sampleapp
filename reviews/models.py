from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from shops.models import Shop

UserModel = get_user_model()


class Review(models.Model):
    """
    レビュー情報のモデル
    各フィールドは reviews_review テーブルのカラムにマッピングされる
    """
    comment = models.CharField(max_length=1000)
    photo = models.ImageField(blank=True, null=True)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def list_latest(cls):
        return cls.objects.order_by('posted_at').reverse()

    def has_score(self):
        return self.score is not None
