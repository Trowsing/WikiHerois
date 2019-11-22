# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.core.urlresolvers import reverse
from django.test import TestCase
from .views import home


class HomeTests(TestCase):
    # Testar se a página inicial funciona
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # Testar se as definições de URL são corretas
    def test_home_url_resolves_home_view(self):
        view = resolve("/")
        self.assertEquals(view.func, home)
