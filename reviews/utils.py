from django.conf import settings


def filter_high_score(reviews):
    return [r for r in reviews if r.score >= settings.HIGH_SCORE]
