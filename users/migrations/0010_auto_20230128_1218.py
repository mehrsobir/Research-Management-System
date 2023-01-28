# Generated by Django 3.2.16 on 2023-01-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_account_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=150, unique=True, verbose_name='email address'),
        ),
    ]
