from .models import Shop


def list_all():
    return Shop.objects.all()


def list_ranking(head=3):
    # TODO get ranking
    return Shop.objects.all()
