# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20141201_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='M', max_length=b'1', verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberfunction',
            name='name',
            field=models.CharField(help_text=b'Ex: Di\xc3\xa1cono', max_length=255, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memberfunction',
            name='nameFemale',
            field=models.CharField(help_text=b'Ex: Diaconisa', max_length=255, verbose_name=b'T\xc3\xadtulo Feminino'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memberfunction',
            name='title',
            field=models.CharField(help_text=b'Ex: Dc', max_length=60, verbose_name=b'T\xc3\xadtulo abrev.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memberfunction',
            name='titleFemale',
            field=models.CharField(help_text=b'Ex: Dc\xc2\xaa', max_length=60, verbose_name=b'T\xc3\xadtulo abrev. Feminino'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_name',
            field=models.CharField(max_length=100, verbose_name=b'Tipo', choices=[(b'CEL', b'Celular'), (b'RES', b'Residencial'), (b'COM', b'Comercial'), (b'FAX', b'Fax'), (b'CLR', b'CLARO'), (b'TIM', b'TIM'), (b'OI', b'OI'), (b'VIV', b'VIVO'), (b'NEX', b'NEXTEL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name=b'N\xc3\xbamero'),
            preserve_default=True,
        ),
    ]
