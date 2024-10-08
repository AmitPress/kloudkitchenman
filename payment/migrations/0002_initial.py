# Generated by Django 5.1.1 on 2024-09-08 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kitchen', '0002_initial'),
        ('payment', '0001_initial'),
        ('stakeholders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='stakeholders.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='kitchen.item'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='users',
            field=models.ManyToManyField(related_name='coupons', to='stakeholders.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='applied_coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='payment.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='stakeholders.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='payment.order'),
        ),
    ]
