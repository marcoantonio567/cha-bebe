# Generated by Django 5.0.1 on 2024-03-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_remove_iten_quantidade"),
    ]

    operations = [
        migrations.AddField(
            model_name="iten",
            name="quantidade",
            field=models.IntegerField(default=0),
        ),
    ]