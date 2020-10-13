#!/usr/bin/env python
# encoding: utf-8
"""
Author: thuync

Copyright (c) 2020 . All rights reserved.
"""
from django.conf import settings
from django.db.models.signals import class_prepared


def add_table_prefix(sender, **kwargs):
    table_prefix = getattr(settings, "TABLE_PREFIX", None)

    app_label = sender._meta.app_label
    app_config = sender._meta.app_config
    app_table_prefix = getattr(app_config, "table_prefix", None)
    table_prefix = app_table_prefix or table_prefix

    if table_prefix:
        current_db_table = sender._meta.db_table
        if current_db_table.startswith(app_label):
            db_table = "_".join([table_prefix, sender._meta.model_name])
            sender._meta.db_table = db_table


class_prepared.connect(add_table_prefix)
