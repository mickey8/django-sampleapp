from django.test import override_settings, SimpleTestCase

from ..models import Review
from ..utils import filter_high_score


class UtilsTest(SimpleTestCase):

    @override_settings(HIGH_SCORE=3)
    def test_filter_high_score(self):
        review1 = Review(id=1, score=2)
        review2 = Review(id=2, score=3)
        review3 = Review(id=3, score=4)

        reviews = filter_high_score([review1, review2, review3])

        self.assertEqual(2, len(reviews))
        self.assertEqual(2, reviews[0].id)
        self.assertEqual(3, reviews[1].id)

    def test_filter_high_score2(self):
        review1 = Review(id=1, score=2)
        review2 = Review(id=2, score=3)
        review3 = Review(id=3, score=4)

        with self.settings(HIGH_SCORE=3):
            reviews = filter_high_score([review1, review2, review3])

            self.assertEqual(2, len(reviews))
            self.assertEqual(2, reviews[0].id)
            self.assertEqual(3, reviews[1].id)

        with self.settings(HIGH_SCORE=4):
            reviews = filter_high_score([review1, review2, review3])

            self.assertEqual(1, len(reviews))
            self.assertEqual(3, reviews[0].id)
