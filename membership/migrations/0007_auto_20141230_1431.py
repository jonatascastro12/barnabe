# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AlterField(
            model_name='person',
            name='member',
            field=models.OneToOneField(verbose_name=b'Membro', to='membership.Member'),
            preserve_default=True,
        ),
    ]
