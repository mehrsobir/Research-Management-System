# Generated by Django 4.0.6 on 2023-01-30 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_plan_subtopic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtopic',
            old_name='plan',
            new_name='plan_id',
        ),
    ]