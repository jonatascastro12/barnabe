# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_name', models.CharField(default=b'Casa', max_length=100)),
                ('address_line', models.CharField(max_length=255, verbose_name=b'Endere\xc3\xa7o')),
                ('city', models.CharField(max_length=255, verbose_name=b'Cidade')),
                ('state', models.CharField(max_length=50, verbose_name=b'UF')),
                ('country', models.CharField(max_length=50, verbose_name=b'Pa\xc3\xads')),
            ],
            options={
                'verbose_name': 'Endere\xe7o',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baptismDt', models.DateField(verbose_name=b'Data de Batismo')),
                ('situation', models.CharField(max_length=7, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'A', b'Ativo'), (b'I', b'Inativo')])),
            ],
            options={
                'verbose_name': 'Membro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=255)),
                ('titleFemale', models.CharField(max_length=60)),
                ('nameFemale', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Fun\xe7\xe3o de membro',
                'verbose_name_plural': 'Fun\xe7\xf5es de membro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('cpf', models.CharField(max_length=14, verbose_name=b'CPF')),
                ('birthDt', models.DateField(verbose_name=b'Data de Nascimento')),
                ('email', models.EmailField(max_length=75)),
                ('member', models.OneToOneField(verbose_name=b'Pessoa', to='membership.Member')),
            ],
            options={
                'verbose_name': 'Pessoa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('person', models.OneToOneField(verbose_name=b'Pessoa', to='membership.Person')),
            ],
            options={
                'verbose_name': 'Telefone',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='memberFunction',
            field=models.ForeignKey(verbose_name=b'Fun\xc3\xa7\xc3\xa3o', to='membership.MemberFunction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.OneToOneField(verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=True,
        ),
    ]
