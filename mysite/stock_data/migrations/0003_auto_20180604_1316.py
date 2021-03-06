# Generated by Django 2.0.4 on 2018-06-04 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_data', '0002_auto_20180603_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='company_name',
            new_name='stock_list',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='stock_symbol',
        ),
        migrations.AddField(
            model_name='stocks',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
