# Generated by Django 5.0 on 2024-01-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_offer_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='owner',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
