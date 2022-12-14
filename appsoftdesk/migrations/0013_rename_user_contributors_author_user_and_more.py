# Generated by Django 4.1.2 on 2022-10-25 19:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("appsoftdesk", "0012_alter_contributors_unique_together"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contributors", old_name="user", new_name="author_user",
        ),
        migrations.AlterUniqueTogether(
            name="contributors", unique_together={("author_user", "project")},
        ),
    ]
