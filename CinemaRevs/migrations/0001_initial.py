# Generated by Django 4.1.2 on 2022-11-16 21:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('duracion', models.IntegerField()),
                ('genero', models.CharField(max_length=40)),
                ('sinopsis', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('texto', models.CharField(max_length=250)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
