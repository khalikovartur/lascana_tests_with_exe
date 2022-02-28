import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner
from unittest import TextTestRunner


current_directory = os.getcwd()

username = "khalikart7" # Replace the username
access_key = "aW5GLG9KKZyYjMC229vvkLMIe50mdt4I9VlKmlMNs1X7Ye4Kjw" # Replace the access key


class LascanaTest(unittest.TestCase):
   
    def setUp(self):
        desired_caps = {
            "build": 'Lascana build', # Change your build name here
            "name": 'Lascana_tests', # Change your test name here
            "browserName": 'Chrome',
            "version": '98.0',
            "platform": 'Windows 10',
            "resolution": '1920x1080',
            "console": 'true', # Enable or disable console logs
            "network": 'true'   # Enable or disable network logs
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities= desired_caps)
        

    def tearDown(self):
        self.driver.quit()
        

    def test_authentication_user(self):
        """ Test go through authentication of an existing user."""
        
        user_name = 'Алла'
        user_mail ='alla@mail.com'
        user_password ='alla1234'
    
        driver = self.driver
        driver.get("https://lascana.ru/")

        user_icon = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__account')
        user_icon.click()

        email = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/label[1]/input')
        email.send_keys(user_mail)

        password = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/label[2]/div/input')
        password.send_keys(user_password)
        
        auth_submit_button = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/div/input')
        auth_submit_button.click()
        time.sleep(2)
        
        name_on_the_header = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__name').text
        self.assertEqual(name_on_the_header, user_name)
        
    def test_registration_new_user(self):
        """New User Registration. To pass the test, enter new data."""
        
        user_name = 'Алла'
        user_last_name = 'Аллова'
        user_mail = 'alllllla@email.com'
        user_password = 'alla1234'
        
        driver = self.driver
        driver.get("https://lascana.ru/")

        user_icon = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__account')
        user_icon.click()

        regis_link = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/div/div[2]/a')
        regis_link.click()
        
        last_name = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[1]/input')
        last_name.send_keys(user_last_name)
        
        name = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[2]/input')
        name.send_keys(user_name)
        
        email = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[4]/input')
        email.send_keys(user_mail)
        
        password = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[5]/input')
        password.send_keys(user_password)
        
        password_confirm  = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[6]/input')
        password_confirm.send_keys(user_password)
        
        agreement_box = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/div[3]/label/span')
        agreement_box.click()
        
        cookies = driver.find_element(by=By.CSS_SELECTOR, value='.cookie-popup')
        driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", cookies)
        
        regis_button = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/div[4]')
        regis_button.click()
        time.sleep(5)
        
        current_url = driver.current_url
        self.assertEqual(current_url, "https://lascana.ru/auth/index.php" )
        
    def test_adding_into_favorites(self):
        """The test adds to favorites and checks the favorites on the favorites' page with the article number."""
        
        driver = self.driver
        driver.get("https://lascana.ru/")
        
        kupalniki_tab = driver.find_element(by=By.CSS_SELECTOR, value='li.navigation-menu__item:nth-child(4) > a:nth-child(1)')
        kupalniki_tab.click()
        
        first_picture = driver.find_element(by=By.XPATH, value='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
        first_picture.click()
        
        icon_add_to_favorite = driver.find_element(by=By.XPATH, value='//*[@id="bx_117848907_7527"]/div[2]/div[4]/a[3]')
        icon_add_to_favorite.click() 
        
        uniq_product_article = driver.find_element(by=By.ID ,value='product__article').text
        
        header_link_into_favorites = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__favourites')
        header_link_into_favorites.click()
        time.sleep(2)
        
        current_url = driver.current_url
        self.assertEqual(current_url, "https://lascana.ru/personal/favorite/" )
        
        favorites_item_image = driver.find_element(by=By.CSS_SELECTOR, value='.personal__favorite--item_image')
        favorites_item_image.click()
        
        product_article_in_favorites = driver.find_element(by=By.ID ,value='product__article').text
        self.assertEqual(uniq_product_article, product_article_in_favorites )
        
    def test_adding_to_shopping_cart(self):
        """The test adds to the shopping cart and checks the product on the carts' page with the article number"""
        
        driver = self.driver
        driver.get("https://lascana.ru/") 
        
        clothes_tab = driver.find_element(by=By.CSS_SELECTOR, value='li.navigation-menu__item:nth-child(3)')    
        clothes_tab.click()
        
        first_picture = driver.find_element(by=By.XPATH, value='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
        first_picture.click()
        
        uniq_product_article = driver.find_element(by=By.ID ,value='product__article').text
        
        button_add_to_cart = driver.find_element(by=By.XPATH, value='//*[@id="bx_117848907_9787_add_basket_link"]')
        button_add_to_cart.click()
        time.sleep(2)
        
        go_to_cart = driver.find_element(by=By.ID, value='go-to-cart__button-cart')
        go_to_cart.click()
        
        
        current_url = driver.current_url
        self.assertEqual(current_url, "https://lascana.ru/personal/cart/")
        
        picture_product_in_the_cart = driver.find_element(by=By.CSS_SELECTOR, value='.cart__item--image')
        picture_product_in_the_cart.click()
        
        product_article_in_cart = driver.find_element(by=By.ID ,value='product__article').text
        self.assertEqual(uniq_product_article, product_article_in_cart)
    
    def test_checking_the_filter_operation_by_price(self):
        """The test sets a price filter and compares the price range against all filtered offers."""
        
        driver = self.driver
        driver.get("https://lascana.ru/")    
        
        min_cost = 2000
        max_cost = 3000 
        
        underwear_tab = driver.find_element(by=By.CSS_SELECTOR, value='li.navigation-menu__item:nth-child(2) > a:nth-child(1)')
        underwear_tab.click()
        
        
        
        min_cost_input_field = driver.find_element(by=By.ID, value='arrFilter_P1_MIN')
        min_cost_input_field.send_keys(min_cost)

        max_cost_input_field = driver.find_element(by=By.ID, value='arrFilter_P1_MAX')
        max_cost_input_field.send_keys(max_cost)
        
        cookies = driver.find_element(by=By.CSS_SELECTOR, value='.cookie-popup')
        driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", cookies)
        time.sleep(2)
        
        set_filter_button = driver.find_element(by=By.ID, value='set_filter')
        set_filter_button.click()
        
        prices_of_all_offers = driver.find_elements(by=By.CLASS_NAME, value='product-card__price-block')
        list_prices = []
        for element in prices_of_all_offers:
            price = ''       
            price = str(element.text)
            list_prices.append(price)
        
        
        prices = [int((price.replace(' ', '')).rstrip('₽')) for price in list_prices]
        for price in prices:
            assert min_cost < price < max_cost
        
class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_lascana_report(self):

        consolidated_test = unittest.TestSuite()

        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(LascanaTest)
            
        ])

        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)
        
class HTMLTestRunner(TextTestRunner):
    """" A test runner class that output the results. """

    time_format = "%Y-%m-%d_%H-%M-%S"

    def __init__(self, output="./reports/", verbosity=2, stream=sys.stderr,
                 descriptions=True, failfast=False, buffer=False,
                 report_title=None, report_name=None, template=None, resultclass=None,
                 add_timestamp=True, open_in_browser=False,
                 combine_reports=False, template_args=None):
        self.verbosity = verbosity
        self.output = output
        self.encoding = 'UTF8'

        TextTestRunner.__init__(self, stream, descriptions, verbosity,
                                failfast=failfast, buffer=buffer)
        

        
if __name__ == "__main__":
    unittest.main()