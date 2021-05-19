from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Steve is looking to use an online to-do app. He goes to the homepage.
        self.browser.get('http://localhost:8000')

        # He sees the page title & header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # He is prompted to enter a to-do item straight away

        # He types "Buy batteries" into a text box.

        # Upon hitting enter, the page updates, and now the page lists
        # "1: Buy batteries" as an item in a to-do list

        # Steve wraps-up his list building

if __name__ == '__main__':
    unittest.main()
