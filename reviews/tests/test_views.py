from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from ..models import Review
from shops.models import Prefecture, Shop


class ReviewListViewTest(TestCase):

    user = None
    shop = None

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user('user@test', 'password')
        prefecture = Prefecture.objects.create(name='東京')
        cls.shop = Shop.objects.create(
            name='name', kana_name='kana name', phone_number='0012345678',
            prefecture=prefecture, address='address'
        )

    def test_get(self):
        """GETリクエスト時のテスト"""
        Review.objects.create(comment='commentA', shop=self.shop, posted_by=self.user)
        Review.objects.create(comment='commentB', shop=self.shop, posted_by=self.user)

        response = self.client.get(reverse('reviews:list'))

        self.assertContains(response, 'commentA')
        self.assertContains(response, 'commentB')


from django.test import tag

@tag('view')
class ReviewCreateViewTest(TestCase):
    """レビュー投稿画面のテストクラス"""

    def test_get_no_login(self):
        """未ログインの場合にログイン画面にリダイレクトされること"""
        response = self.client.get(reverse('reviews:create'))
        self.assertRedirects(
            response, '%s?next=%s' % (
                reverse('login'), reverse('reviews:create')
            )
        )

    def test_get_logged_in(self):
        """ログイン済みの場合にレビュー投稿画面が表示されること"""
        get_user_model().objects.create_user('user@test', 'password')
        self.client.login(username='user@test', password='password')

        response = self.client.get(reverse('reviews:create'))
        self.assertEqual(200, response.status_code)
