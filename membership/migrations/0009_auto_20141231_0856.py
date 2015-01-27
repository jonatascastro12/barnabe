# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20141230_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='member',
        ),
        migrations.AddField(
            model_name='member',
            name='person',
            field=models.OneToOneField(default=1, verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=False,
        ),
    ]
