# Generated by Django 5.1.5 on 2025-01-19 18:53

import django.core.validators
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                (
                    "category",
                    models.CharField(
                        choices=[("Development", "Development"), ("Other", "Other")],
                        max_length=20,
                    ),
                ),
                ("read_length", models.IntegerField()),
                (
                    "publication_date",
                    models.DateField(
                        verbose_name="Date when the article was published."
                    ),
                ),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="article_images",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                    ),
                ),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "tags",
                    models.CharField(
                        blank=True,
                        help_text="Comma-separated list of tags",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("views", models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "ordering": ["-publication_date"],
            },
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                (
                    "source",
                    models.CharField(
                        choices=[("Udemy", "Udemy"), ("Other", "Other (Specify)")],
                        default="Other",
                        max_length=50,
                    ),
                ),
                (
                    "source_custom",
                    models.CharField(
                        blank=True,
                        help_text="Specify if Other",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("date_issued", models.DateField(blank=True, null=True)),
                (
                    "icon",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="certification_icons/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg", "svg"]
                            )
                        ],
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Certificate",
                "verbose_name_plural": "Certificates",
                "ordering": ["-date_issued"],
            },
        ),
        migrations.CreateModel(
            name="ClientOpinion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=12)),
                ("occupation", models.CharField(max_length=20)),
                ("content", models.TextField()),
                (
                    "stars",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Opinion",
                "verbose_name_plural": "Client Opinions",
            },
        ),
        migrations.CreateModel(
            name="ExpertArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=10)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="expert_area_icons",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name": "Expert Area",
                "verbose_name_plural": "Expert Areas",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("availability", models.BooleanField(default=True)),
                ("github", models.URLField()),
                ("linkedin", models.URLField()),
                ("discord", models.URLField()),
                ("client_count", models.PositiveIntegerField(default=0)),
                ("projects_completed", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("overview", models.TextField(blank=True, null=True)),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, null=True, verbose_name="Description"
                    ),
                ),
                (
                    "short_description",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="project_images",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                    ),
                ),
                ("client", models.CharField(blank=True, max_length=100, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, max_length=150, unique=True)),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="service_images",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg", "svg"]
                            )
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=10)),
                ("company_name", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Work Experience",
                "verbose_name_plural": "Work Experiences",
            },
        ),
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="project_images/additional_images",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_images",
                        to="main.project",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="services",
            field=models.ManyToManyField(blank=True, to="main.service"),
        ),
    ]
