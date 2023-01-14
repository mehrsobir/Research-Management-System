# Generated by Django 3.2.16 on 2023-01-14 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constant', '0002_delete_degree'),
        ('users', '0006_auto_20230114_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constant.education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('М', 'Мард'), ('З', 'Зан')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constant.nationality'),
        ),
    ]
