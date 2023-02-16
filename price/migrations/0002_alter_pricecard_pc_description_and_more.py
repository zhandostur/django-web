# Generated by Django 4.1.6 on 2023-02-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecard',
            name='pc_description',
            field=models.CharField(max_length=20, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pricecard',
            name='pc_value',
            field=models.CharField(max_length=20, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='pt_new_price',
            field=models.CharField(max_length=20, verbose_name='Новая цена'),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='pt_old_price',
            field=models.CharField(max_length=20, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='pt_title',
            field=models.CharField(max_length=20, verbose_name='Услуги'),
        ),
    ]