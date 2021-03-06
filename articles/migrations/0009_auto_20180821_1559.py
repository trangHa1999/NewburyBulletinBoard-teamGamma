# Generated by Django 2.0.6 on 2018-08-21 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_auto_20180813_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='vetted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='vettedBy',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='vettedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='roomNumber',
            field=models.CharField(default='AC008', max_length=8),
        ),
    ]
