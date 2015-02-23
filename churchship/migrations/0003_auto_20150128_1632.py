# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('churchship', '0002_auto_20150128_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='address_line',
            field=models.CharField(blank=True, max_length=b'300', null=True, verbose_name=b'Endere\xc3\xa7o', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='city',
            field=models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Cidade', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='email',
            field=models.EmailField(max_length=b'200', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Bairro', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'N\xe3o \xe9 permitido caraceteres especiais.')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='state',
            field=models.CharField(blank=True, max_length=b'2', null=True, verbose_name=b'UF', choices=[(b'', b'Selecione um estado'), (b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AM', b'Amazonas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maranh\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernambuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')]),
            preserve_default=True,
        ),
    ]
