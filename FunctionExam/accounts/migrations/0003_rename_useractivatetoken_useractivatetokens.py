# Generated by Django 3.2.12 on 2022-04-06 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220406_0848'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserActivateToken',
            new_name='UserActivateTokens',
        ),
    ]