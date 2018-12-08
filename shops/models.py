import logging

from django.db import models

log = logging.getLogger(__name__)


class Prefecture(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Budget(models.Model):
    lowest = models.IntegerField()
    highest = models.IntegerField()


class Shop(models.Model):
    name = models.CharField(max_length=128)
    kana_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    @classmethod
    def list_all(cls):
        return cls.objects.all()

    @classmethod
    def list_ranking(cls, head=None):
        return sorted(
            cls.objects.all().prefetch_related('review_set'),
            key=lambda x: x.score, reverse=True
        )[0:head]

    @property
    def score(self):
        scores = [r.score for r in self.review_set.all() if r.score]
        return sum(scores) / len(scores) if scores else 0

    def __str__(self):
        return self.name


class ShopProfile(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    access = models.CharField(max_length=255)
    business_hours = models.CharField(max_length=255)
    regular_holiday = models.CharField(max_length=255)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    url = models.URLField()
