# Generated by Django 4.0.6 on 2023-01-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_article_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(),
        ),
    ]