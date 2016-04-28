# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0003_auto_20160425_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='selling_price',
            field=models.DecimalField(max_digits=15, decimal_places=2, default=123.0),
            preserve_default=False,
        ),
    ]
