# Generated by Django 5.0 on 2024-01-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating_value',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None),
        ),
    ]
