# Generated by Django 5.0.6 on 2024-08-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertarea',
            name='image',
            field=models.ImageField(upload_to='expert_area_icons'),
        ),
        migrations.AlterField(
            model_name='expertarea',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]