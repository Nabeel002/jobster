# Generated by Django 4.0.5 on 2022-09-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0015_jobs_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company_name',
            field=models.CharField(default=1, max_length=150),
        ),
    ]