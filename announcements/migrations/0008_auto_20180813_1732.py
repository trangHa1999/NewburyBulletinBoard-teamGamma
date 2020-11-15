# Generated by Django 2.0.6 on 2018-08-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0007_announcement_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='color',
            field=models.CharField(choices=[('', 'None'), ('bg-primary', 'Primary'), ('bg-secondary', 'Secondary'), ('bg-success', 'Success'), ('bg-info', 'Info'), ('bg-warning', 'Warning'), ('bg-danger', 'Danger'), ('bg-light', 'Light'), ('bg-dark', 'Dark')], default='None', max_length=15),
        ),
    ]