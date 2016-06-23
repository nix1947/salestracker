# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0009_auto_20160623_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='clearance',
            name='description',
            field=models.CharField(default='something paid', max_length=15),
            preserve_default=False,
        ),
    ]
