from django.test import TestCase

from store.models import Category, Offer

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='hostels', slug='hostels')


    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'hostels')

class TestOffersModel(TestCase):
    def setUp(self):
        self.data1 = Offer.objects.create(category='hostels', owned_by='owner', name='Double Lux', slug='double-lux',
                                          location='Paris', price=10000, rating=2, is_available=True, is_active=True, period='M',
                                          room_type='double bed')


    def test_offer_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Offer))

    def test_offer_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'hostels')