# Generated by Django 4.2.7 on 2023-12-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player_info", "0003_alter_record_ballcourse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opponent",
            name="opponent_date",
            field=models.DateTimeField(default=""),
        ),
        migrations.AlterField(
            model_name="record",
            name="ballcourse",
            field=models.IntegerField(default=0),
        ),
    ]
