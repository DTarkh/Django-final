# Generated by Django 5.1.4 on 2024-12-05 06:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.PositiveIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('brand', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thumbnail', models.URLField()),
                ('category', models.ManyToManyField(to='store.category')),
            ],
        ),
    ]
