from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        #We are wanting to verify that the root of the site goes to home_page
        found = resolve('/')
        self.assertEqual(found.func, home_page)
