# Generated by Django 2.2.13 on 2020-08-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0009_auto_20200624_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatelog',
            name='datetime',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Datetime'),
        ),
    ]