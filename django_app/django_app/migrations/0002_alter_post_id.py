# Generated by Django 4.2.9 on 2024-01-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
