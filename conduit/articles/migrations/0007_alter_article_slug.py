# Generated by Django 5.1.3 on 2024-12-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_slug_uid_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(editable=False, max_length=68),
        ),
    ]
