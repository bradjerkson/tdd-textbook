from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Steve is looking to use an online to-do app. He goes to the homepage.
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: Buy batteries')


        #There's still a text box inviting him to add another item.
        #he enters "put batteries into remote"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('put batteries into remote')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #The page updates again, and now shows both items on his list
        self.check_for_row_in_list_table('1: Buy batteries')
        self.check_for_row_in_list_table('2: put batteries into remote')

        #Edith wonders whether the site will remember her list.
        #She sees that the site has generated a unique URL for her.
        self.fail('Finish the test!')
        # Steve wraps-up his list building


if __name__ == '__main__':
    unittest.main()
