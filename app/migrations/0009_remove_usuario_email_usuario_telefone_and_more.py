# Generated by Django 5.0.1 on 2024-03-26 04:55

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_usuario_delete_usuarios"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="email",
        ),
        migrations.AddField(
            model_name="usuario",
            name="telefone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="", max_length=128, region=None
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="data_pedida",
            field=models.DateTimeField(),
        ),
    ]