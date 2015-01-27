# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('discipleship', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipler',
            options={'verbose_name': 'Discipulador', 'verbose_name_plural': 'Discipuladores'},
        ),
        migrations.AlterModelOptions(
            name='meeting',
            options={'verbose_name': 'Reuni\xe3o', 'verbose_name_plural': 'Reuni\xf5es'},
        ),
        migrations.AlterField(
            model_name='disciple',
            name='discipler',
            field=models.ForeignKey(verbose_name=b'Discipulador', to='discipleship.Discipler'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciple',
            name='member',
            field=models.ForeignKey(verbose_name=b'Membro', to='membership.Member'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='datetime',
            field=models.DateTimeField(verbose_name=b'Hor\xc3\xa1rio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='description',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='disciple',
            field=models.ForeignKey(verbose_name=b'Discipulo', to='discipleship.Disciple'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='discipler',
            field=models.ForeignKey(verbose_name=b'Discipulador', to='discipleship.Discipler'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='monitors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Monitor'),
            preserve_default=True,
        ),
    ]
