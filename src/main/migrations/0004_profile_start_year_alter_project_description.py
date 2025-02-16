# Generated by Django 5.1.5 on 2025-01-31 17:01

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_contactmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="start_year",
            field=models.PositiveIntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
