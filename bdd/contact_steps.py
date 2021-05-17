from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given("a contact list")
def contact_list(db):
    return db.get_contact_list()


@given("a contact with <firstname>, <middlename>, <address> , <lastname> , <company> , <homephone> , <mobilephone> , <workphone> , <secondaryphone> , <email> , <email2> , <email3>")
def new_contact(firstname, middlename, address, lastname, company, homephone, workphone, secondaryphone, email, email2, email3 ):
    return Contact(firstname=firstname, middlename=middlename, address=address, lastname=lastname, company=company, homephone=homephone,
                   workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then("the new contact list is equal to the old list with the added new contact")
def verify_contact_added(db, app, check_ui, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given("a non-empty contact list")
def non_empty_contact_list(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname",middlename="mid2",lastname="lastname"))
    return db.get_contact_list()


@given("a random contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I delete the contact from the list")
def delete_random_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then("the new contact list is equal to the old contact list without the deleted contact")
def verify_contact_deleted(db, app, check_ui, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@when("I modify the contact from the list")
def delete_random_contact(app, random_contact, new_contact):
    new_contact.id = random_contact.id
    app.contact.edit_contact_by_id(new_contact, random_contact.id)


@then("the new contact list is equal to the old contact list with the modified contact")
def verify_contact_modified(db, check_ui, app, non_empty_contact_list, new_contact, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_group_list()
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)