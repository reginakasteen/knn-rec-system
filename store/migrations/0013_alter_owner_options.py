# Generated by Django 5.0 on 2024-02-21 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_offer_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ('owner_name',), 'verbose_name_plural': 'owners'},
        ),
    ]
