# Generated by Django 5.1.3 on 2024-12-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_slug_uuid_article_uuid_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug_uuid',
            field=models.SlugField(editable=False, max_length=100),
        ),
    ]
