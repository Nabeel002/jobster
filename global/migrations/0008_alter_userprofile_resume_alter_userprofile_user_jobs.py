# Generated by Django 4.0.5 on 2022-09-05 21:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('global', '0007_userprofile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, default='documents/yk_sugi_resume_new.docx', null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('request_text', models.TextField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_poster', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
