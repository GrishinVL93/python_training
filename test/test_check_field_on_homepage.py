import re

from model.contact import Contact


def test_contact_fields_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()[0]
    contacts_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.lastname == clear(contacts_from_edit_page.lastname)
    assert contacts_from_home_page.firstname == clear(contacts_from_edit_page.firstname)
    assert contacts_from_home_page.address == clear(contacts_from_edit_page.address)
    assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_edit_page)
    assert contacts_from_home_page.all_emails_from_home_page == merge_emails_lies_on_home_page(contacts_from_edit_page)


def test_contact_fields_on_home_page_and_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    for elem in contacts_from_home_page:
        assert contacts_from_home_page[index].lastname == contacts_from_db[index].lastname
        assert contacts_from_home_page[index].firstname == contacts_from_db[index].firstname
        assert contacts_from_home_page[index].address == contacts_from_db[index].address
        assert contacts_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert contacts_from_home_page[index].all_emails_from_home_page == merge_emails_lies_on_home_page(contacts_from_db[index])
        index = index + 1


def test_phone_on_contact_view_page(app):
    contacts_from_view_page = app.contact.get_contact_from_view_page(0)
    contacts_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contacts_from_view_page.homephone == contacts_from_edit_page.homephone
    assert contacts_from_view_page.workphone == contacts_from_edit_page.workphone
    assert contacts_from_view_page.mobilephone == contacts_from_edit_page.mobilephone
    assert contacts_from_view_page.secondaryphone == contacts_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_lies_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))