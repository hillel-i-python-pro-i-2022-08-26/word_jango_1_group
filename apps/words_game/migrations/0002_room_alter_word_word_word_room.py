# Generated by Django 4.1.2 on 2022-10-21 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("words_game", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("host", models.CharField(max_length=50)),
                ("last_word", models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name="word",
            name="word",
            field=models.CharField(max_length=70),
        ),
        migrations.AddField(
            model_name="word",
            name="room",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="words", to="words_game.room"
            ),
        ),
    ]
