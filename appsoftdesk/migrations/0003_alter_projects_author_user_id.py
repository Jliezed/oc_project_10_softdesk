# Generated by Django 4.1.2 on 2022-10-07 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("appsoftdesk", "0002_alter_projects_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="author_user_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]