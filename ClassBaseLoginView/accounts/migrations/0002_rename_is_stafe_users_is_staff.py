# Generated by Django 3.2.12 on 2022-05-02 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='is_stafe',
            new_name='is_staff',
        ),
    ]
