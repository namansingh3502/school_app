# Generated by Django 3.1.4 on 2021-01-10 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.class'),
        ),
        migrations.AddField(
            model_name='permission',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.subject'),
        ),
        migrations.AddField(
            model_name='permission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
