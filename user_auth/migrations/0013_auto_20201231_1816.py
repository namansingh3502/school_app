# Generated by Django 3.1.4 on 2020-12-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0012_auto_20201231_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_login',
            field=models.BooleanField(),
        ),
    ]
