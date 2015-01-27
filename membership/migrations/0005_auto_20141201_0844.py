# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20141201_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='phone_name',
            new_name='phone_type',
        ),
    ]
