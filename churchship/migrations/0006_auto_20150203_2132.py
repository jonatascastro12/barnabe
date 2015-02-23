# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0005_auto_20150129_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='churchtype',
            options={'verbose_name': 'Tipo de Igreja'},
        ),
    ]
