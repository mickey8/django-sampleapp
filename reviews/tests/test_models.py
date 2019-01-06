from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Review
from shops.models import Prefecture, Shop

UserModel = get_user_model()


class ReviewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UserModel.objects.create_user('user@test', 'pwd')
        prefecture = Prefecture.objects.create(name='東京')
        Shop.objects.create(
            name='name', kana_name='kana name', phone_number='0012345678',
            prefecture=prefecture, address='address'
        )

    def test_has_score(self):
        review1 = Review()
        review2 = Review(score=1)

        self.assertFalse(review1.has_score())
        self.assertTrue(review2.has_score())

    def test_list_latest(self):
        shop = Shop.objects.get(pk=1)
        user = get_user_model().objects.get(pk=1)
        Review.objects.create(comment='commentA', score=1, shop=shop, posted_by=user)
        Review.objects.create(comment='commentB', score=1, shop=shop, posted_by=user)

        reviews = Review.list_latest()

        self.assertEqual(2, len(reviews))
        self.assertEqual('commentB', reviews[0].comment)
        self.assertEqual('commentA', reviews[1].comment)
