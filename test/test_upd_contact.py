from model.contact import Contact


def test_upd_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.update(Contact("Updated", "Updated", "Updated", "Updated", "Updated", "Udated",
                            "Updated", "Updated", "Updated", "Updated",
                            "Updated", "Updated", "Updated"))
    app.session.logout()
