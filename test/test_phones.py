import re


def test_phone_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()[0]
    contacts_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_edit_page)


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
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))