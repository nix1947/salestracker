# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0008_auto_20160623_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='clearnce',
        ),
        migrations.AddField(
            model_name='clearance',
            name='company',
            field=models.ForeignKey(to='salesmanager.Company', default=1),
            preserve_default=False,
        ),
    ]
