# Generated by Django 4.1.2 on 2022-10-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appsoftdesk", "0007_rename_author_user_id_comments_author_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects", name="title", field=models.CharField(max_length=250),
        ),
    ]