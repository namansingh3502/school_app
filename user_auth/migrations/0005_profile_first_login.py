# Generated by Django 3.1.2 on 2020-11-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20201115_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
    ]