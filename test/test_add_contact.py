# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Vlad", "Grishin", "Petrov", "VlGrishin", "Engineer", "RTS COMPANY",
                            "Moscow, Tverskaya street 34, h30", "+78999990073", "+79383434624", "GrishinTest@mail.ru",
                            "Adress Test", "Home Test", "Some notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
