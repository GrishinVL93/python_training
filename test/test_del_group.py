from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Empty test group"))
    app.group.del_first_group()
