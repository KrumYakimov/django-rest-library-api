# Generated by Django 5.1.3 on 2024-11-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
