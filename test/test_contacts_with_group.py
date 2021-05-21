from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app, db, orm):
    groups = orm.get_group_list()
    if len(groups) == 0:
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

    contact = random.choice(orm.get_contact_list())
    group = random.choice(groups)

    contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    if contact in contacts_in_group:
        app.contact.create(Contact(firstname='NotInGroupFirstName',
                                   lastname='NotInGroupLastName',
                                   middlename='NotInGroupMiddleName'))

    contact = random.choice(orm.get_contacts_not_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_after_add = orm.get_contacts_in_group(Group(id=group.id))
    assert contact in contacts_after_add


def test_delete_contact_from_group(app, db, orm):
    if len(orm.get_group_list()) == 0:
        new_group = Group(name='NAME GROUP',
                          header='HEADER',
                          footer='FOOTER')
        app.group.create(new_group)

    if len(orm.get_contact_list()) == 0:
        new_contact = Contact(firstname='First Name',
                              lastname='Last Name',
                              middlename='Middle Name')
        app.contact.create(new_contact)

    groups = db.get_group_list()
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    group = random.choice(groups)

    contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    if contact not in contacts_in_group:
        app.contact.add_contact_to_group(contact.id, group.id)
    app.contact.delete_contact_from_group(contact.id, group.id)
    contacts_after_del = orm.get_contacts_in_group(Group(id=group.id))
    assert contact not in contacts_after_del
