from model.contact import Contact
from random import randrange


def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Empty Contact", "My Contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.del_contact_by_id(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts