# Generated by Django 4.2.8 on 2023-12-09 10:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_blogpost_delete_post"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BlogPost",
            new_name="Post",
        ),
    ]