# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0010_auto_20141231_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo_crop_data',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='photo_original',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='address_line',
            field=models.CharField(blank=True, max_length=b'300', verbose_name=b'Endere\xc3\xa7o', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=b'200', verbose_name=b'Cidade', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name=b'CPF', validators=[django.core.validators.RegexValidator(b'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', 'Voc\xea deve digitar os 11 d\xedgitos do seu CPF.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nome', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.', flags=4)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=b'200', verbose_name=b'Bairro', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to=b'members/', verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
