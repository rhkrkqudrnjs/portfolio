# Generated by Django 4.2.7 on 2023-12-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player_info", "0010_alter_opponent_opponent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opponent",
            name="opponent_date",
            field=models.DateField(default=""),
        ),
    ]
