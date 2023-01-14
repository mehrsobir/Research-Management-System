# Generated by Django 3.2.16 on 2023-01-14 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constant', '0001_initial'),
        ('institutions', '0002_auto_20230114_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='founded_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='founded_at',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField(default=1)),
                ('occupied', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('degree_needed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constant.degree')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.department')),
            ],
            options={
                'verbose_name': 'Вазифа',
                'verbose_name_plural': 'Вазифаҳо',
            },
        ),
    ]
