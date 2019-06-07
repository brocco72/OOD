# Generated by Django 2.0 on 2019-06-07 12:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190524_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Provider')),
            ],
        ),
        migrations.RemoveField(
            model_name='sellinvoice',
            name='total_price',
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
