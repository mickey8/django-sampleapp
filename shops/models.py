import logging

from django.core.cache import cache
from django.db import models

log = logging.getLogger(__name__)

_KEY_PREFECTURES = '_all_prefectures'


class Prefecture(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        prefectures = cache.get(_KEY_PREFECTURES)
        if not prefectures:
            log.debug('No prefectures in cache.')
            prefectures = cls.objects.all()
            cache.set(_KEY_PREFECTURES, prefectures)
        return prefectures


class Budget(models.Model):
    lowest = models.IntegerField()
    highest = models.IntegerField()


class Shop(models.Model):
    name = models.CharField(max_length=128)
    kana_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShopProfile(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    access = models.CharField(max_length=255)
    business_hours = models.CharField(max_length=255)
    regular_holiday = models.CharField(max_length=255)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    url = models.URLField()
