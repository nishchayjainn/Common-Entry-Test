# Generated by Django 3.0.5 on 2020-04-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accountmodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='text',
            field=models.BooleanField(default=False),
        ),
    ]
