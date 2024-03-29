# Generated by Django 4.0.6 on 2023-01-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('founded_at', models.DateTimeField()),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
    ]
