# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0003_auto_20150128_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarnabeUserChurch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission', models.CharField(default=b'ADM', max_length=30, choices=[(b'ADM', b'administrator'), (b'EDT', b'editor'), (b'VW', b'viewer')])),
                ('barnabe_user', models.OneToOneField(to='churchship.BarnabeUser')),
                ('church', models.OneToOneField(to='churchship.Church')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='church',
            name='barnabe_user',
        ),
        migrations.AddField(
            model_name='barnabeuser',
            name='is_supervisor',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barnabeuser',
            name='supervisor',
            field=models.ForeignKey(blank=True, to='churchship.BarnabeUser', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='is_mother',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
