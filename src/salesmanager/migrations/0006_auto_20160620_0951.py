# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0005_auto_20160620_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 20, 9, 51, 21, 432865, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 20, 9, 51, 26, 985983, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
