# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class DatabasesConfig(AppConfig):
    name = 'databases'

    def ready(self):
        import databases.signals.database
