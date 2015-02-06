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
                'verbose_name_plural': 'Discipuladores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name=b'Hor\xc3\xa1rio')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('disciple', models.ForeignKey(verbose_name=b'Discipulo', to='discipleship.Disciple')),
                ('discipler', models.ForeignKey(verbose_name=b'Discipulador', to='discipleship.Discipler')),
                ('monitors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Monitor')),
            ],
            options={
                'verbose_name': 'Reuni\xe3o',
                'verbose_name_plural': 'Reuni\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='disciple',
            name='discipler',
            field=models.ForeignKey(verbose_name=b'Discipulador', to='discipleship.Discipler'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciple',
            name='member',
            field=models.ForeignKey(verbose_name=b'Membro', to='membership.Member'),
            preserve_default=True,
        ),
    ]
