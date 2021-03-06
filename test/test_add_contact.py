# -*- coding: utf-8 -*-
from model.contact import Contact
# import pytest
# import random
# import string


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

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
