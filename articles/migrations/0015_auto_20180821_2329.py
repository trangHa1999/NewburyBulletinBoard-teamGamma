# Generated by Django 2.0.6 on 2018-08-21 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_semester_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='classSchedules',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ClassSchedule'),
        ),
    ]
