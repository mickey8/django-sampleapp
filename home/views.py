from django.http import HttpResponse
from django.views.generic import TemplateView, View

from reviews.models import Review
from shops.models import Shop


class TopView(TemplateView):
    template_name = 'home/top.html'

    def get_context_data(self, **kwargs):
        kwargs['shop_list'] = Shop.list_ranking(head=3)
        kwargs['review_list'] = Review.list_latest()[:10]
        return super().get_context_data(**kwargs)


class StatusView(View):

    def get(self, request):
        return HttpResponse('動画投稿アプリは正常に起動しています。')
