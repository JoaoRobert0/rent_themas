# Generated by Django 4.0 on 2024-08-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_rent_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='first_purchase',
            field=models.BooleanField(default=True),
        ),
    ]
