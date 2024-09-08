# Generated by Django 5.1.1 on 2024-09-08 18:07

import helpers.timestampedmodel
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('DEBIT', 'debit'), ('CREDIT', 'credit')], default='CREDIT', max_length=256)),
                ('number', models.IntegerField()),
                ('cvv', models.CharField(max_length=64)),
                ('expiration', models.DateField()),
                ('postal_code', models.IntegerField()),
                ('status', models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], default='ACTIVE', max_length=256)),
            ],
            bases=(models.Model, helpers.timestampedmodel.TimeStampedModelMixin),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
            bases=(models.Model, helpers.timestampedmodel.TimeStampedModelMixin),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('occasion', models.TextField(max_length=512)),
                ('discount', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], default='ACTIVE', max_length=256)),
            ],
            bases=(models.Model, helpers.timestampedmodel.TimeStampedModelMixin),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('PLACED', 'placed'), ('INPROCESS', 'inprocess'), ('DELIVERED', 'delivered'), ('COMPLETED', 'completed'), ('DISCARDED', 'discarded')], default='PLACED', max_length=256)),
                ('total_price', models.FloatField(default=0.0)),
                ('discounted_price', models.FloatField(default=0.0)),
            ],
            bases=(models.Model, helpers.timestampedmodel.TimeStampedModelMixin),
        ),
    ]
