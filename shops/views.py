from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView

from .forms import ShopCreateForm
from .models import Shop


class ShopRankingView(LoginRequiredMixin, ListView):
    model = Shop
    template_name = 'shops/shop_list.html'

    def get_queryset(self):
        return self.model.list_ranking()


class ShopCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        """GETリクエスト用のメソッド"""

        # テンプレートに渡す変数の dict を作成
        context = {
            # 空のフォーム
            'form': ShopCreateForm(),
        }
        # 空のフォームをテンプレートにレンダリングしたコンテンツを保持した HttpResponse を返す
        return render(request, 'shops/shop_form.html', context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""

        # リクエストからフォームを作成
        form = ShopCreateForm(request.POST)

        # バリデーション実行
        if not form.is_valid():
            # バリデーションNGの場合はテンプレートを再表示する
            return render(request, 'shops/shop_form.html', {'form': form})

        # ショップ情報を作成
        form_data = form.cleaned_data
        Shop(
            name=form_data['name'],
            kana_name=form_data['kana_name'],
            phone_number=form_data['phone_number'],
            prefecture=form_data['prefecture'],
            address=form_data['address']
        ).save()

        # 次画面にリダイレクト
        return redirect(reverse_lazy('top'))
