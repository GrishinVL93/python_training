

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):
        # login
        wd = self.app.wd
        self.app.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
