from conftest import check_ui
from model.contact import Contact
import random

from model.group import Group


def test_del_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("Empty Contact", "My Contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_del_random_contact_from_group(app, orm):
    new_group = None
    new_contact = None

    group_list = orm.get_group_list()
    if len(group_list) == 0:
        new_group = Group(name='NAME GROUP',
                          header='HEADER',
                          footer='FOOTER')
        app.group.create(new_group)

    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        new_contact = Contact(firstname='First Name',
                              lastname='Last Name',
                              middlename='Middle Name')
        app.contact.create(new_contact)

  #  contacts = list()
    group = Group(id='[none]')
    flag = False

    if new_group is not None:
        if new_contact is not None:
            app.contact.select_contact_by_id(new_contact.id)
            app.contact.add_contact_to_selected_group(new_group)

    for gr in group_list:
        count_contacts = orm.get_count_contacts_in_group(Group(id=gr.id))
        if count_contacts > 0:
            group = gr
            contacts = orm.get_contacts_in_group(Group(id=gr.id))
            flag = True
            break

    if not flag:
        groups = orm.get_group_list()
        group = groups[random.randint(0, len(groups)-1)]
        contact = contacts[random.randint(0, len(contacts)-1)]
        app.contact.select_contact_by_id(contact.id)
        app.contact.add_contact_to_selected_group(group)

    if flag:
        contact = contacts[random.randint(0, len(contacts)-1)]

    app.contact.set_listgroup_for_contacts(group)
    app.contact.select_contact_by_id(contact.id)
    app.contact.delete_contact_from_selected_group()
    assert orm.contact_in_group(contact, group) == False