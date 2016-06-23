# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0004_item_selling_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('paid_value', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(verbose_name='Purchase price', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='selling_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
