# Generated by Django 5.0.1 on 2024-03-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0022_alter_usuario_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="iten",
            name="quantidade",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
