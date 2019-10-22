# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20191019_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(),
        ),
    ]
