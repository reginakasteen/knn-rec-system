# Generated by Django 5.0 on 2024-01-29 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_offer_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='rating',
        ),
    ]
