# Generated by Django 5.0.6 on 2024-10-28 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_remove_article_overview_project_overview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='content',
        ),
    ]
