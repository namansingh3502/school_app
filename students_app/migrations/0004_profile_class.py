# Generated by Django 3.1.4 on 2021-01-17 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0002_auto_20210116_1101'),
        ('students_app', '0003_auto_20210116_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='class_app.profile'),
            preserve_default=False,
        ),
    ]
