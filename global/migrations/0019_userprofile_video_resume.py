# Generated by Django 4.0.5 on 2022-09-09 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0018_jobrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='video_resume',
            field=models.FileField(blank=True, default='documents/video_file.mp4', null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]
