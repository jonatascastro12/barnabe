# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0004_auto_20150129_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barnabeuserchurch',
            name='barnabe_user',
            field=models.ForeignKey(to='churchship.BarnabeUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barnabeuserchurch',
            name='church',
            field=models.ForeignKey(to='churchship.Church'),
            preserve_default=True,
        ),
    ]
