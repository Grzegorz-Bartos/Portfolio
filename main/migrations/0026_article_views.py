# Generated by Django 5.0.6 on 2024-10-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_article_content_article_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
