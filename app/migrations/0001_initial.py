# Generated by Django 5.0.3 on 2024-03-25 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inten",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=40)),
                ("ativo", models.BooleanField(default=True)),
                ("quantidade", models.IntegerField()),
                ("data_pedido", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
