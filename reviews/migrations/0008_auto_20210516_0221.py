# Generated by Django 3.1 on 2021-05-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_book_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.TextField(verbose_name='Text summary of the book'),
        ),
    ]
