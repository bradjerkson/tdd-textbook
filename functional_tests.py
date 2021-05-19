from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is prompted to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Buy batteries" into a text box.
        inputbox.send_keys('Buy batteries')

        # Upon hitting enter, the page updates, and now the page lists
        # "1: Buy batteries" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy batteries', [row.text for row in rows])
        #There's still a text box inviting him to add another item.
        #he enters "put batteries into remote"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('put batteries into remote')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #The page updates again, and now shows both items on his list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy batteries', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly', [row.text for row in rows]
        )

        #Edith wonders whether the site will remember her list.
        #She sees that the site has generated a unique URL for her.
        self.fail('Finish the test!')
        # Steve wraps-up his list building


if __name__ == '__main__':
    unittest.main()
