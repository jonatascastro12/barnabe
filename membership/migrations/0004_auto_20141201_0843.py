# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20141201_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_name',
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.CharField(default=b'Casa', max_length=100, verbose_name=b'Tipo', choices=[(b'RES', b'Residencial'), (b'COM', b'Comercial')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phone',
            name='ramal',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Ramal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_name',
            field=models.CharField(max_length=100, verbose_name=b'Tipo', choices=[(b'FRE', b'Fixo Residencial'), (b'FCO', b'Fixo Comercial'), (b'FAX', b'Fax'), (b'CLR', b'CLARO'), (b'TIM', b'TIM'), (b'OI', b'OI'), (b'VIV', b'VIVO'), (b'NEX', b'NEXTEL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name=b'N\xc2\xba Telefone'),
            preserve_default=True,
        ),
    ]
