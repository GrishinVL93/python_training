from model.contact import Contact


def test_modify_firstname(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="New FIRSTNAME"))
    app.session.logout()


def test_modify_lastname(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(lastname="New LASTNAME"))
    app.session.logout()


def test_modify_middlename(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(middlename="New MIDDLENAME"))
    app.session.logout()


def test_modify_main_fields(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact("Updated", "Updated", "Updated", "Updated", "Updated", "Udated",
                            "Updated", "Updated", "Updated", "Updated",
                            "Updated", "Updated", "Updated"))
    app.session.logout()
