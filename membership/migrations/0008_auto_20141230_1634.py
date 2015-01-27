# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_auto_20141230_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='person',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='person',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.AddField(
            model_name='person',
            name='address_line',
            field=models.CharField(default='Av. Brasil', max_length=b'300', verbose_name=b'Endere\xc3\xa7o', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='Rio de Janeiro', max_length=b'200', verbose_name=b'Cidade', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='neighborhood',
            field=models.CharField(default='Jardim Guanabara', max_length=b'200', verbose_name=b'Bairro', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone1',
            field=models.CharField(default=5555555, max_length=b'15', verbose_name=b'Telefone 1', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone2',
            field=models.CharField(default=5555555, max_length=b'15', verbose_name=b'Telefone 2', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='foto.jpg', upload_to=b'uploaded_images', verbose_name=b'Foto', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(default='RJ', max_length=b'2', verbose_name=b'UF', blank=True, choices=[(b'', b'Selecione um estado'), (b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AM', b'Amazonas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maranh\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernambuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=b'200'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='member',
            field=models.OneToOneField(null=True, verbose_name=b'Membro', to='membership.Member'),
            preserve_default=True,
        ),
    ]
