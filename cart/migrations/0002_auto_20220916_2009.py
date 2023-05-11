# Generated by Django 3.2.15 on 2022-09-16 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_products_options'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartlist',
            options={'verbose_name': 'cartlist', 'verbose_name_plural': 'cartlists'},
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quan', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
    ]