# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0007_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clearance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paid_value', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PaymentStatus',
        ),
        migrations.AddField(
            model_name='company',
            name='clearnce',
            field=models.ForeignKey(default=1, to='salesmanager.Clearance'),
            preserve_default=False,
        ),
    ]
