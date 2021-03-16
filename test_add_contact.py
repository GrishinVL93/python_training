# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"


    def test_add_contact(self):
        driver = self.driver
        driver.get("https://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("LoginForm").submit()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Vlad")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Grishin")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Petrov")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("VlGrishin")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Engineer")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("RTS COMPANY")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Moscow, Tverskaya street 34, h30")
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("+78999990073")
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("+79383434624")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("GrishinTest@mail.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("10")
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("October")
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1991")
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("Adress Test")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("Home Test")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Some notes")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
