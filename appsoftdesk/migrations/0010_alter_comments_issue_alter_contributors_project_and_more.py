# Generated by Django 4.1.2 on 2022-10-14 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("appsoftdesk", "0009_alter_projects_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="issue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="appsoftdesk.issues",
            ),
        ),
        migrations.AlterField(
            model_name="contributors",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="contributors",
                to="appsoftdesk.projects",
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="priority",
            field=models.CharField(
                choices=[
                    ("faible", "faible"),
                    ("moyenne", "moyenne"),
                    ("élevée", "élevée"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="status",
            field=models.CharField(
                choices=[
                    ("à faire", "à faire"),
                    ("en cours", "en cours"),
                    ("à terminé", "à terminé"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="tag",
            field=models.CharField(
                choices=[
                    ("à faire", "à faire"),
                    ("en cours", "en cours"),
                    ("à terminé", "à terminé"),
                ],
                max_length=250,
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="title",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
