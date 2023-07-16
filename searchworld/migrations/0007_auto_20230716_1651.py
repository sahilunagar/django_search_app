# Generated by Django 3.2.7 on 2023-07-16 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchworld', '0006_delete_countrylanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=30)),
                ('is_official', models.CharField(choices=[('T', 'T'), ('F', 'F')], default='F', max_length=1)),
                ('percentage', models.FloatField(default=0.0)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchworld.country')),
            ],
        ),
        migrations.AddConstraint(
            model_name='countrylanguage',
            constraint=models.UniqueConstraint(fields=('country_code', 'language'), name='UX01_country_langauge'),
        ),
    ]