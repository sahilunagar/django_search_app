from django.db import models

class Country(models.Model):
    continent_choices = [
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
        ('South America', 'South America'),
    ]

    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=52)
    continent = models.CharField(max_length=13, choices=continent_choices, default='Asia')
    region = models.CharField(max_length=26)
    surface_area = models.FloatField(default=0.00)
    indep_year = models.SmallIntegerField(null=True)
    population = models.IntegerField(default=0)
    life_expectancy = models.FloatField(null=True)
    gnp = models.FloatField(null=True)
    gnp_old = models.FloatField(null=True)
    local_name = models.CharField(max_length=45)
    government_form = models.CharField(max_length=45)
    head_of_state = models.CharField(max_length=60, null=True)
    capital = models.IntegerField(null=True)
    code2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    # country_code = models.CharField(max_length=3)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    district = models.CharField(max_length=20)
    population = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CountryLanguage(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['country_code', 'language'], name = 'UX01_country_langauge')
        ]
    id = models.AutoField(primary_key=True)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=30)
    is_official = models.CharField(max_length=1, choices=(('T', 'T'), ('F', 'F')), default='F')
    percentage = models.FloatField(default=0.0)

    def __str__(self):
        return self.language
