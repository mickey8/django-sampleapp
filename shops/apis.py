from .models import Shop


def all():
    return Shop.objects.all()
