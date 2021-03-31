from model.contact import Contact


def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New FIRSTNAME"))


def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New LASTNAME"))


def test_modify_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="New MIDDLENAME"))


def test_modify_main_fields(app):
    app.contact.modify_first_contact(Contact("Updated", "Updated", "Updated", "Updated", "Updated", "Udated",
                            "Updated", "Updated", "Updated", "Updated",
                            "Updated", "Updated", "Updated"))
