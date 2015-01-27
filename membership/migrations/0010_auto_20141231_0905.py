# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20141231_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='person',
            field=models.OneToOneField(null=True, verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=True,
        ),
    ]
