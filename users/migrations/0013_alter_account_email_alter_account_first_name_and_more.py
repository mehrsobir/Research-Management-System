# Generated by Django 4.0.6 on 2023-01-30 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constant', '0003_category_direction_status'),
        ('users', '0012_alter_account_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Ном'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Насаб'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constant.education', verbose_name='Маълумот'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('М', 'Мард'), ('З', 'Зан')], max_length=1, null=True, verbose_name='Ҷинс'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='img/user.png', null=True, upload_to='images/user_images', verbose_name='Расм'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constant.nationality', verbose_name='Миллат'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Телефон'),
        ),
    ]
