from .models import Review


def all():
    return Review.objects.all()
