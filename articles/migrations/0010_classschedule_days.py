# Generated by Django 2.0.6 on 2018-08-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20180821_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='days',
            field=models.CharField(default='', max_length=20),
        ),
    ]
