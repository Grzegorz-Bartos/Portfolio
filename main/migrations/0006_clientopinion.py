# Generated by Django 5.0.6 on 2024-08-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_project_description_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=12)),
                ('content', models.TextField()),
                ('stars', models.IntegerField()),
            ],
        ),
    ]