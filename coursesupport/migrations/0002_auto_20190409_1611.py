# Generated by Django 2.1.7 on 2019-04-09 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesupport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='text',
            new_name='summaryText',
        ),
    ]