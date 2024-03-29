# Generated by Django 4.0.6 on 2023-01-13 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_education_nationality_alter_profile_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/user_images', verbose_name='Расм'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.nationality'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
