# Generated by Django 3.2.16 on 2023-01-28 06:15

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_book_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='static/pdf/scientific', validators=[main.validators.validate_file_extension], verbose_name='PDF-Файл'),
        ),
        migrations.AlterField(
            model_name='article_pub',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='static/pdf/public', validators=[main.validators.validate_file_extension], verbose_name='PDF-Файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='static/pdf/books', validators=[main.validators.validate_file_extension], verbose_name='PDF-Файл'),
        ),
    ]
