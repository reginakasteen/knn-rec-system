# Generated by Django 5.0 on 2024-01-26 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_review_rating_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
    ]
