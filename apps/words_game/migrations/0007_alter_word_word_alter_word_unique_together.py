# Generated by Django 4.1.2 on 2022-10-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("words_game", "0006_alter_word_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="word",
            field=models.CharField(max_length=70),
        ),
        migrations.AlterUniqueTogether(
            name="word",
            unique_together={("word", "room")},
        ),
    ]
