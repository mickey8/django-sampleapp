from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from shops.models import Shop

UserModel = get_user_model()


class Review(models.Model):
    """
    口コミ情報のモデル
    各フィールドは reviews_review テーブルのカラムにマッピングされる
    """
    # コメント
    comment = models.CharField(max_length=1000)
    # 画像
    photo = models.ImageField(blank=True, null=True)
    # 評価点数
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    # ショップ（Shop モデルへの外部参照）
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # 投稿者。ユーザーモデルへの外部参照
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # 投稿日時
    posted_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def list_latest(cls):
        return cls.objects.order_by('posted_at').reverse()

    def has_score(self):
        return self.score is not None
