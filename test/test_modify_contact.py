from model.contact import Contact
from random import randrange


def test_modify_firstname(app):
    app.contact.open_contact_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="For Modify Test", lastname="For Modify Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New FIRSTNAME", lastname="New LASTNAME")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

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
