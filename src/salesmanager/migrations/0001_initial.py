# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Pant', 'pant'), ('Shirt', 'shirt'), ('T-shirt', 't-shirt'), ('shoes', 'Shoes')], default='pant', max_length=100, verbose_name='Item Category')),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Item Category',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=9)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesmanager.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Item name')),
                ('tag', models.CharField(max_length=30, unique=True, verbose_name='Item tag')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesmanager.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesmanager.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='company',
            name='contact_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesmanager.ContactPerson'),
        ),
    ]
