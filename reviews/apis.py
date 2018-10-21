from .models import Review


def list_all():
    return Review.objects.all()


def list_latest():
    # TODO get latest
    return Review.objects.all()
