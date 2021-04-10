from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Empty test group"))
    old_groups = app.group.get_group_list()
    app.group.del_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)