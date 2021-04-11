from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, data):
        # Заполняем поля и создаем контакт
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(data)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.companyname)
        self.type("address", contact.addresscompany)
        self.type("home", contact.phone)
        self.type("mobile", contact.mobilephone)
        self.type("email", contact.email)
        self.type("address2", contact.address2)
        self.type("phone2", contact.additionalphone)
        self.type("notes", contact.notes)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def del_first_contact(self):
        wd = self.app.wd
        # select first group
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirmation deletion contact
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//a[img[@title='Edit']]").click()
        # open modification form
        # wd.find_element_by_name("edit").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") or wd.current_url.endswith("addressbook/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)
