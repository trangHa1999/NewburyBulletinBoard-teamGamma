# Generated by Django 2.0.6 on 2018-08-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20180821_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='year',
            new_name='semesterYear',
        ),
        migrations.AlterField(
            model_name='article',
            name='modificationDate',
            field=models.DateField(auto_now=True),
        ),
    ]
