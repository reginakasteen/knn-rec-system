# Generated by Django 5.0 on 2024-02-21 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_alter_viewhistory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewhistory',
            options={'verbose_name_plural': 'views'},
        ),
    ]
