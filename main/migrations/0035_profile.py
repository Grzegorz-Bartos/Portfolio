# Generated by Django 5.0.6 on 2024-11-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_project_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years_of_experience', models.PositiveIntegerField(default=3)),
                ('availability', models.BooleanField(default=True)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('discord', models.URLField()),
                ('client_count', models.PositiveIntegerField(default=0)),
                ('projects_completed', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]