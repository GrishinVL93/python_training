from model.contact import Contact


def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("For Modify Test"))
    app.contact.modify_first_contact(Contact(firstname="New FIRSTNAME"))


def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("For Modify Test"))
    app.contact.modify_first_contact(Contact(lastname="New LASTNAME"))


def test_modify_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("For Modify Test"))
    app.contact.modify_first_contact(Contact(middlename="New MIDDLENAME"))


def test_modify_main_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("For Modify Test"))
    app.contact.modify_first_contact(Contact("Updated", "Updated", "Updated", "Updated", "Updated", "Udated",
                            "Updated", "Updated", "Updated", "Updated",
                            "Updated", "Updated", "Updated"))
