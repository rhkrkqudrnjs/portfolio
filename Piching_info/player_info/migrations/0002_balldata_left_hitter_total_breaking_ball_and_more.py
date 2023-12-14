# Generated by Django 4.2.7 on 2023-11-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player_info", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="balldata",
            name="left_hitter_total_breaking_ball",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="left_hitter_total_fast_ball",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="left_hitter_total_pitches",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="left_hitter_total_speed_off_ball",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="right_hitter_total_breaking_ball",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="right_hitter_total_fast_ball",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="right_hitter_total_pitches",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="balldata",
            name="right_hitter_total_speed_off_ball",
            field=models.IntegerField(default=0),
        ),
    ]
