# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"

    def test_add_contact(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd, "admin", "secret")
        self.open_contact_page(wd)
        self.create_contact(wd, "Vlad", "Grishin", "Petrov", "VlGrishin", "Engineer", "RTS COMPANY",
                            "Moscow, Tverskaya street 34, h30", "+78999990073", "+79383434624", "GrishinTest@mail.ru",
                            "Adress Test", "Home Test", "Some notes")
        self.logout(wd)

    def logout(self, wd):
        # Выход из приложения
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd, firstname, middlename, lastname, nickname, title, companyname, addresscompany, phone,
                       mobilephone, email, address2, additionalphone, notes):
        # Заполняем поля и создаем контакт
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % companyname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % addresscompany)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % mobilephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % email)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % additionalphone)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self, wd):
        # Открываем страницу создания контакта
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, name, password):
        # Авторизация в приложении
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_id("LoginForm").submit()

    def open_page(self, wd):
        # Открываем стартовую страницу
        wd.get("https://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
