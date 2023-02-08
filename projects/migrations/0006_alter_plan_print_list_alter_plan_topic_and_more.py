# Generated by Django 4.0.6 on 2023-02-07 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_plan_print_list_subtopic_print_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='print_list',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Ҷузъи чопӣ'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.topic', verbose_name='Мавзуъ'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Сол'),
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('user', 'year')},
        ),
    ]