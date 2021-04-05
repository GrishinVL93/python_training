from model.contact import Contact


def test_del_first_contact(app):
    app.contact.open_contact_page()
    if app.contact.count() == 0:
        app.contact.create(Contact("Empty Contact"))
    app.contact.del_first_contact()

