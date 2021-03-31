# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("Vlad", "Grishin", "Petrov", "VlGrishin", "Engineer", "RTS COMPANY",
                            "Moscow, Tverskaya street 34, h30", "+78999990073", "+79383434624", "GrishinTest@mail.ru",
                            "Adress Test", "Home Test", "Some notes"))

