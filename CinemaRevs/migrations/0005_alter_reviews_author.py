# Generated by Django 4.1.2 on 2022-12-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaRevs', '0004_rename_images_reviews_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='author',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]