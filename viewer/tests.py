from django.test import TestCase


class ExampleTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        #print('setUpTestData: Spustí se jednou na začátku testování a '
        #      'slouží k nastavení/naplnění databáze.')
        pass

    def setUp(self):
        #print('setUp: Spustí se před každým testem.')
        pass

    def test_false(self):
        #print("Testovací metoda: test_false")
        result = False  # reálně výsledek práce s projektem/databází
        self.assertFalse(result)

    def test_add(self):
        #print("Testovací metoda: test_add")
        result = 4 + 1
        self.assertEqual(result, 5)
