# Generated by Django 2.0.4 on 2018-06-03 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks_man',
            new_name='Stocks',
        ),
        migrations.DeleteModel(
            name='Cool',
        ),
    ]
