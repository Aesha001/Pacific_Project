# Generated by Django 4.0.6 on 2023-02-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_stourbooking_travel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_tours',
            name='boarding_point',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='special_tours',
            name='dropping_point',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
