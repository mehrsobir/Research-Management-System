# Generated by Django 3.2.16 on 2023-01-15 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230115_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user_job',
            name='job',
        ),
        migrations.RemoveField(
            model_name='user_job',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='radio',
            options={'verbose_name': 'Барномаи радиоӣ', 'verbose_name_plural': 'Барномаҳои радиоӣ'},
        ),
        migrations.AlterModelOptions(
            name='tv',
            options={'verbose_name': 'Барномаи телевизионӣ', 'verbose_name_plural': 'Барномаҳои телевизионӣ'},
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='Subtopic',
        ),
        migrations.DeleteModel(
            name='User_job',
        ),
    ]
