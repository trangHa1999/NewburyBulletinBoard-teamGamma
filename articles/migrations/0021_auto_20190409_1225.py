# Generated by Django 2.1.7 on 2019-04-09 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20180823_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='vettedBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vettedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]