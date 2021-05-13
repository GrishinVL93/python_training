from conftest import check_ui
from model.group import Group
import random

def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For updated"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_data = Group(name="Updated", footer="Footer updated", header="Header Updated")
    app.group.modify_group_by_id(group.id, new_data)
    new_groups = db.get_group_list()
    index = 0
    for g in old_groups:
        if g.id == group.id:
            break
        index = index + 1
    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="For updated"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)



