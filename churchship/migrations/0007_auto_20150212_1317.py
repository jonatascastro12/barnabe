# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0006_auto_20150203_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barnabeuser',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='barnabeuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='barnabeuserchurch',
            name='barnabe_user',
        ),
        migrations.DeleteModel(
            name='BarnabeUser',
        ),
        migrations.RemoveField(
            model_name='barnabeuserchurch',
            name='church',
        ),
        migrations.DeleteModel(
            name='BarnabeUserChurch',
        ),
    ]
