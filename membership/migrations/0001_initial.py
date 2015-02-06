# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baptismDt', models.DateField(verbose_name=b'Data de Batismo')),
                ('situation', models.CharField(max_length=7, verbose_name=b'Situa\xc3\xa7\xc3\xa3o', choices=[(b'A', b'Ativo'), (b'I', b'Inativo')])),
                ('church', models.ForeignKey(to='churchship.Church')),
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
                ('title', models.CharField(help_text=b'Ex: Dc', max_length=60, verbose_name=b'T\xc3\xadtulo abrev.')),
                ('name', models.CharField(help_text=b'Ex: Di\xc3\xa1cono', max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('titleFemale', models.CharField(help_text=b'Ex: Dc\xc2\xaa', max_length=60, verbose_name=b'T\xc3\xadtulo abrev. Feminino')),
                ('nameFemale', models.CharField(help_text=b'Ex: Diaconisa', max_length=255, verbose_name=b'T\xc3\xadtulo Feminino')),
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
                ('name', models.CharField(max_length=255, verbose_name=b'Nome', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.', flags=4)])),
                ('cpf', models.CharField(max_length=14, verbose_name=b'CPF', validators=[django.core.validators.RegexValidator(b'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', 'Voc\xea deve digitar os 11 d\xedgitos do seu CPF.')])),
                ('birthDt', models.DateField(verbose_name=b'Data de Nascimento')),
                ('gender', models.CharField(max_length=b'1', verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('email', models.EmailField(max_length=b'200')),
                ('address_line', models.CharField(blank=True, max_length=b'300', verbose_name=b'Endere\xc3\xa7o', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')])),
                ('neighborhood', models.CharField(blank=True, max_length=b'200', verbose_name=b'Bairro', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')])),
                ('city', models.CharField(blank=True, max_length=b'200', verbose_name=b'Cidade', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')])),
                ('state', models.CharField(blank=True, max_length=b'2', verbose_name=b'UF', choices=[(b'', b'Selecione um estado'), (b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AM', b'Amazonas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maranh\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernambuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')])),
                ('phone1', models.CharField(max_length=b'15', verbose_name=b'Telefone 1', blank=True)),
                ('phone2', models.CharField(max_length=b'15', verbose_name=b'Telefone 2', blank=True)),
                ('photo', models.ImageField(upload_to=b'members/', verbose_name=b'Foto', blank=True)),
                ('photo_original', models.CharField(max_length=255, null=True)),
                ('photo_crop_data', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Pessoa',
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
            model_name='member',
            name='person',
            field=models.OneToOneField(null=True, verbose_name=b'Pessoa', to='membership.Person'),
            preserve_default=True,
        ),
    ]
