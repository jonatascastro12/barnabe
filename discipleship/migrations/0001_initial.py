# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Discipulo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', models.ForeignKey(to='membership.Member')),
            ],
            options={
                'verbose_name': 'Discipulador',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('disciple', models.ForeignKey(to='discipleship.Disciple')),
                ('discipler', models.ForeignKey(to='discipleship.Discipler')),
                ('monitors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reuni\xe3o',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='disciple',
            name='discipler',
            field=models.ForeignKey(to='discipleship.Discipler'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciple',
            name='member',
            field=models.ForeignKey(to='membership.Member'),
            preserve_default=True,
        ),
    ]
