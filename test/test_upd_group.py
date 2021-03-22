from model.group import Group


def test_upd_first_group(app):
    app.session.login("admin", "secret")
    app.group.update(Group("Updated Group", "Updated Info", "Updated foot"))
    app.session.logout()
