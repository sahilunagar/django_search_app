# Generated by Django 3.2.7 on 2023-07-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchworld', '0002_auto_20230716_1616'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='countrylanguage',
            constraint=models.UniqueConstraint(fields=('country_code', 'language'), name='UX01_country_langauge'),
        ),
    ]