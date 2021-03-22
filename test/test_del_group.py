

def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.group.del_first_group()
    app.session.logout()
