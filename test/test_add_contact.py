# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):

    app.session.login("admin", "secret")
    app.contact.create(Contact("Vlad", "Grishin", "Petrov", "VlGrishin", "Engineer", "RTS COMPANY",
                            "Moscow, Tverskaya street 34, h30", "+78999990073", "+79383434624", "GrishinTest@mail.ru",
                            "Adress Test", "Home Test", "Some notes"))
    app.session.logout()
