# Generated by Django 4.0.5 on 2022-09-09 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('global', '0012_alter_jobs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
