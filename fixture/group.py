

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        # init group creation
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
