# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.BooleanField(default=True, verbose_name='New or Sold'),
        ),
    ]
