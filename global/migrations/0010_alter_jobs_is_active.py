# Generated by Django 4.0.5 on 2022-09-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0009_alter_jobs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]