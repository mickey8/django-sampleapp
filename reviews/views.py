from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, ListView

from .forms import ReviewCreateForm
from .models import Review
from shops.models import Shop


class ReviewListView(ListView):
    model = Review

    def get_queryset(self):
        return self.model.list_latest()


class ReviewCreateView(LoginRequiredMixin, View):
    """レビュー登録画面のビュー"""

    def get(self, request, *args, **kwargs):
        """GETリクエスト用のメソッド"""

        # テンプレートに渡す変数の dict を作成
        context = {
            # 空のフォーム
            'form': ReviewCreateForm(),
        }
        # 空のフォームをテンプレートにレンダリングしたコンテンツを保持した HttpResponse を返す
        return render(request, 'reviews/review_form.html', context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""

        # リクエストからフォームを作成
        form = ReviewCreateForm(request.POST, request.FILES)

        # バリデーション実行
        if not form.is_valid():
            # バリデーションNGの場合はテンプレートを再表示する
            render(request, 'reviews/review_form.html', {'form': form})

        # レビュー情報を作成
        form_data = form.cleaned_data
        Review(
            comment=form_data['comment'],
            photo=form_data['photo'],
            score=form_data['score'],
            shop=Shop.objects.get(pk=form_data['shop']),
            posted_by=request.user
        ).save()

        # 次画面にリダイレクト
        return redirect(reverse_lazy('top'))

"""
class ReviewCreateView(FormView):
    form_class = ReviewCreateForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.save()
        return super().form_valid(form)
"""
