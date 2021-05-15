# -*- coding: utf-8 -*-
from model.contact import Contact
import random
from model.group import Group
# import pytest
# import random
# import string


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_random_contact_to_group(app, orm):
    new_group = None
    new_contact = None
    groups = orm.get_group_list()
    if len(groups) == 0:
        new_group = Group(name='NAME',
                          header='HEADER',
                          footer='FOOTER')
        app.group.create(new_group)
    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        new_contact = Contact(firstname='FIRSTNAME',
                              lastname='LASTNAME',
                              middlename='MIDDLENAME')
        app.contact.create(new_contact)
    if new_group is None:
        index = random.randint(0, len(groups) - 1)
        new_group = groups[index]
        if new_contact is None:
            for new_group in groups:
                contacts = orm.get_contacts_not_in_group(new_group)
                if len(contacts) != 0:
                    index = random.randint(0, len(contacts) - 1)
                    new_contact = contacts[index]
                    break
    app.contact.select_contact_by_id(new_contact.id)
    app.contact.add_contact_to_selected_group(new_group)
    assert orm.contact_in_group(new_contact, new_group) == True


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " " * 10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Contact(firstname="", lastname="", homephone="",
#                     workphone="", mobilephone="", secondaryphone="")] + [
#                Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
#                        homephone=random_string("homephone", 10),
#                        workphone=random_string("workphone", 10), mobilephone=random_string("mobilephone", 10),
#                        secondaryphone=random_string("secondary", 10))
#                for i in range(5)
#            ]


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_add_contact(app, contact):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
