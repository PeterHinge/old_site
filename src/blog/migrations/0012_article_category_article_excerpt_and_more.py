# Generated by Django 4.2.3 on 2023-07-24 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_article_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='key_words',
            field=models.CharField(max_length=100),
        ),
    ]
