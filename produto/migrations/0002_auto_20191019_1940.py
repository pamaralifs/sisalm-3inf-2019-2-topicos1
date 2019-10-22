# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(max_length=20, default='Material de consumo', choices=[('Material de consumo', 'Material de consumo'), ('Material permanente', 'Material permanente')]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(verbose_name='Nome', max_length=50),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(max_length=7),
        ),
    ]
