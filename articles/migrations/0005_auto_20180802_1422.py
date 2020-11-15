# Generated by Django 2.0.6 on 2018-08-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='articles/images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='qrcCodeImage',
            field=models.ImageField(blank=True, upload_to='articles/images/qrc/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='subjectArea',
            field=models.CharField(choices=[('general', 'General'), ('programming1', 'Programming 1'), ('programming2', 'Programming 2'), ('programming3', 'Programming 3'), ('web-client-development', 'Web Client Development'), ('web-server-development', 'Web Server Development'), ('web-design', 'Web Design'), ('databases', 'Databases'), ('networking1', 'Networking 1'), ('networking2', 'Networking 2'), ('security1', 'Cyber Security 1'), ('security2', 'Cyber Security 2'), ('linux', 'Linux'), ('embedded', 'Embedded Systems'), ('python', 'Python'), ('c', 'C/C++'), ('java', 'Java'), ('javascript', 'Javascript'), ('servers', 'Servers')], default=1, max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='subjectAreaSecondary',
            field=models.CharField(blank=True, choices=[('general', 'General'), ('programming1', 'Programming 1'), ('programming2', 'Programming 2'), ('programming3', 'Programming 3'), ('web-client-development', 'Web Client Development'), ('web-server-development', 'Web Server Development'), ('web-design', 'Web Design'), ('databases', 'Databases'), ('networking1', 'Networking 1'), ('networking2', 'Networking 2'), ('security1', 'Cyber Security 1'), ('security2', 'Cyber Security 2'), ('linux', 'Linux'), ('embedded', 'Embedded Systems'), ('python', 'Python'), ('c', 'C/C++'), ('java', 'Java'), ('javascript', 'Javascript'), ('servers', 'Servers')], max_length=30),
        ),
    ]