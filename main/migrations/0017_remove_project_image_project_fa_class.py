# Generated by Django 5.0.6 on 2024-10-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_projectimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='fa_class',
            field=models.TextField(blank=True, null=True),
        ),
    ]