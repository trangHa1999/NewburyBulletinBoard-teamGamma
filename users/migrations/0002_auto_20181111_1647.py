# Generated by Django 2.0.6 on 2018-11-11 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activationExpires',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='activationString',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
