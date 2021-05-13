from conftest import check_ui
from model.contact import Contact
import random


def test_modify_firstname(app, db):
    app.contact.open_contact_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="For Modify Test", lastname="For Modify Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_data = Contact(firstname="New FIRSTNAME", lastname="New LASTNAME")
    app.contact.modify_contact_by_id(contact.id, new_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = 0
    for c in old_contacts:
        if c.id == contact.id:
            break
        index = index + 1
    new_data.id = contact.id
    old_contacts[index] = new_data
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_lastname(app):
#    app.contact.open_contact_page()
#    if app.contact.count() == 0:
#        app.contact.create(Contact("For Modify Test"))
#    app.contact.modify_first_contact(Contact(lastname="New LASTNAME"))


# def test_modify_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact("For Modify Test"))
#    app.contact.modify_first_contact(Contact(middlename="New MIDDLENAME"))


# def test_modify_main_fields(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact("For Modify Test"))
#    app.contact.modify_first_contact(Contact("Updated", "Updated", "Updated", "Updated", "Updated", "Udated",
#                            "Updated", "Updated", "Updated", "Updated",
#                            "Updated", "Updated", "Updated"))
