# Generated by Django 5.0.1 on 2024-03-26 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_remove_usuario_email_usuario_telefone_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Inten",
            new_name="Iten",
        ),
    ]
