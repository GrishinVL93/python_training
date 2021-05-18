# -*- coding: utf-8 -*-
import pytest
import allure
from model.group import Group


# import pytest
# from data.groups import constant as testdata

def test_add_group(app, db, json_groups):
    group = json_groups
    with allure.step("a group list"):
        old_groups = db.get_group_list()
    with allure.step("I add the group to the list"):
        app.group.create(group)
    with allure.step("the new group list is equal to the old list with the added new group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, group):
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
