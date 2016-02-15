from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Firefox()
       # implicit waits
       self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check out its homepage
        self.browser.get('http://localhost:8000')

        # notices page title and header information
        self.assertIn( 'To-Do', self.browser.title)
        self.fail('Finish the test!')
# She is inted to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# She types "Buy peacok feather" into a text box

# When she hits enter, the page updates and now the page lists
# 1. Buy peacock feathers to make a fly

# The page updates again, now shows both items on her list

# Edith wonders whether the site will remember her lis. Then she sees
# that the site has generated a unique URL for her - there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still here.

# Satisfiued, she goes back to sleep

