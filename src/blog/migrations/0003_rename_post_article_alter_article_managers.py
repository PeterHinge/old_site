# Generated by Django 4.2.3 on 2023-07-24 03:56

from django.conf import settings
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_post_options_alter_post_slug_alter_post_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('all_articles', django.db.models.manager.Manager()),
            ],
        ),
    ]
