

def test_phone_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()[0]
    contacts_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.phone
