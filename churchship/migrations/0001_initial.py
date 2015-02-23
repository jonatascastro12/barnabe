# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BarnabeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=20, verbose_name=b'CNPJ', blank=True)),
                ('phone1', models.CharField(max_length=15, verbose_name='Telefone 1', blank=True)),
                ('phone2', models.CharField(max_length=15, verbose_name='Telefone 2', blank=True)),
                ('logo', models.ImageField(upload_to=b'church/', verbose_name=b'Logo', blank=True)),
                ('logo_original', models.CharField(max_length=255, null=True)),
                ('logo_crop_data', models.CharField(max_length=255, null=True)),
                ('barnabe_user', models.ForeignKey(to='churchship.BarnabeUser')),
                ('church_mother', models.ForeignKey(blank=True, to='churchship.Church', null=True)),
            ],
            options={
                'verbose_name': 'Igreja',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChurchType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tipo de igreja',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='church',
            name='type',
            field=models.ForeignKey(to='churchship.ChurchType'),
            preserve_default=True,
        ),
    ]
