# Generated by Django 5.0.1 on 2024-03-26 18:52

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_iten_quantidade_alter_usuario_data_pedida_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="telefone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, default=None, max_length=128, region=None
            ),
        ),
    ]
