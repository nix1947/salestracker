# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0006_auto_20160620_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, default='surfer.manoj@gmail.com'),
            preserve_default=False,
        ),
    ]
