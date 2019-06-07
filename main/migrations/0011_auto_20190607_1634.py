# Generated by Django 2.0 on 2019-06-07 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190607_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyInvoiceItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='buyinvoice',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sellinvoice',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sellinvoiceitems',
            name='off',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='customerleveloff',
            name='off',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='off',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sellinvoiceitems',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_invoice', to='main.SellInvoice'),
        ),
        migrations.AlterField(
            model_name='sellinvoiceitems',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sellinvoiceitems',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sellinvoiceitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_item_product', to='main.Product'),
        ),
        migrations.AddField(
            model_name='buyinvoiceitems',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_invoice', to='main.BuyInvoice'),
        ),
        migrations.AddField(
            model_name='buyinvoiceitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_item_product', to='main.Product'),
        ),
    ]
