# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=True,
        ),
    ]
