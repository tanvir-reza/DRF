# Generated by Django 5.0.3 on 2024-03-16 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_book_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='author',
            name='bod',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]