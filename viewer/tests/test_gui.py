import time
from unittest import skip

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GuiTestWithSelenium(TestCase):
    @skip
    def test_home_page(self):
        drivers = [webdriver.Firefox(), webdriver.Chrome()]
        for driver in drivers:
            driver.get('http://127.0.0.1:8000/')
            time.sleep(2)

            username_field = driver.find_element(By.ID, 'id_username')
            username_field.send_keys('test_user')
            time.sleep(2)

            pswd_field = driver.find_element(By.ID, 'id_password')
            pswd_field.send_keys('SuperTajneHeslo123!')
            time.sleep(2)

            submit_button = driver.find_element(By.ID, 'id_submit')
            submit_button.send_keys(Keys.RETURN)
            time.sleep(2)

            assert "Vítejte ve filmové databázi HollyMovies." in driver.page_source

    @skip
    def test_signup(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/accounts/signup/')
        time.sleep(2)

        username_field = driver.find_element(By.ID, 'id_username')
        username_field.send_keys('TestUser')
        time.sleep(2)

        first_name_field = driver.find_element(By.ID, 'id_first_name')
        first_name_field.send_keys('Testovací')
        time.sleep(2)

        last_name_field = driver.find_element(By.ID, 'id_last_name')
        last_name_field.send_keys('Tester')
        time.sleep(2)

        email_field = driver.find_element(By.ID, 'id_email')
        email_field.send_keys('tester@hollymovies.com')
        time.sleep(2)

        pswd1_field = driver.find_element(By.ID, 'id_password1')
        pswd1_field.send_keys('SuperTajneHeslo123!')
        time.sleep(2)

        pswd2_field = driver.find_element(By.ID, 'id_password2')
        pswd2_field.send_keys('SuperTajneHeslo123!')
        time.sleep(2)

        date_of_birth_field = driver.find_element(By.ID, 'id_date_of_birth')
        date_of_birth_field.send_keys('2003-10-15')
        time.sleep(2)

        biography_field = driver.find_element(By.ID, 'id_biography')
        biography_field.send_keys('Já jsem hlavní tester.')
        time.sleep(2)

        phone_field = driver.find_element(By.ID, 'id_phone')
        phone_field.send_keys('777123456')
        time.sleep(2)

        submit_button = driver.find_element(By.ID, 'id_submit')
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        assert ('Username:'
                or 'A user with that username already exists.'
                in driver.page_source)

    @skip
    def test_signup_date_in_future(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/accounts/signup/')
        time.sleep(2)

        username_field = driver.find_element(By.ID, 'id_username')
        username_field.send_keys('TestUser1')
        time.sleep(2)

        first_name_field = driver.find_element(By.ID, 'id_first_name')
        first_name_field.send_keys('Testovací')
        time.sleep(2)

        last_name_field = driver.find_element(By.ID, 'id_last_name')
        last_name_field.send_keys('Tester')
        time.sleep(2)

        email_field = driver.find_element(By.ID, 'id_email')
        email_field.send_keys('tester@hollymovies.com')
        time.sleep(2)

        pswd1_field = driver.find_element(By.ID, 'id_password1')
        pswd1_field.send_keys('SuperTajneHeslo123!')
        time.sleep(2)

        pswd2_field = driver.find_element(By.ID, 'id_password2')
        pswd2_field.send_keys('SuperTajneHeslo123!')
        time.sleep(2)

        date_of_birth_field = driver.find_element(By.ID, 'id_date_of_birth')
        date_of_birth_field.send_keys('2033-10-15')
        time.sleep(2)

        biography_field = driver.find_element(By.ID, 'id_biography')
        biography_field.send_keys('Já jsem hlavní tester.')
        time.sleep(2)

        phone_field = driver.find_element(By.ID, 'id_phone')
        phone_field.send_keys('777123456')
        time.sleep(2)

        submit_button = driver.find_element(By.ID, 'id_submit')
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Datum narození nesmí být v budoucnosti.' in driver.page_source

    @skip
    def test_movie_not_in_db(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/movie/65646/')
        time.sleep(2)

        assert 'Chyba 404: Stránka nenalezena' in driver.page_source