from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Empty Contact"))
    app.contact.del_first_contact()

