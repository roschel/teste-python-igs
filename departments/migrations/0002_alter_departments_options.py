# Generated by Django 4.1.7 on 2023-03-30 17:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="departments",
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
            },
        ),
    ]