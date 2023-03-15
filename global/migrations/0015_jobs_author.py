# Generated by Django 4.0.5 on 2022-09-09 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('global', '0014_remove_jobs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]