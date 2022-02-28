# Generated by Django 3.2.12 on 2022-02-28 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0005_add_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 7, 57, 38, 144991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 7, 57, 38, 145034, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('authors', models.ManyToManyField(to='ModelApp.Authors')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
