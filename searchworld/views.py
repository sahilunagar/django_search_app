from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Country, City, CountryLanguage

def search(request):
    if request.method == 'POST':
        search_text = request.POST['searchtext']

        #temporary code ends
        if search_text:
            # Query cities
            city_results = City.objects.filter(name=search_text)
            cities = [city.id for city in city_results]
            if len(cities):
                request.session['city_id'] = cities[0]
                return redirect('city_description')

            # Query countries
            country_results = Country.objects.filter(name=search_text)
            countries = [country.code for country in country_results]
            if len(countries):
                request.session['country_code'] = countries[0]
                return redirect('country_description')

            # Query languages
            language_results = CountryLanguage.objects.filter(language=search_text)
            languages = [language.id for language in language_results]
            if len(languages):
                request.session['lang_id'] = languages
                return redirect('language_description')

    return render(request, 'search.html')

def search_autosuggest(request):
    search_text = request.GET.get('search_text')

    # Perform the autosuggest query based on the search_text
    # Replace the following logic with your actual search implementation

    suggestions = []

    #temporary code ends
    if search_text:
        # Query cities
        city_results = City.objects.filter(name__icontains=search_text)[:5]
        suggestions.extend([city.name for city in city_results])

        # Query countries
        country_results = Country.objects.filter(name__icontains=search_text)[:5]
        suggestions.extend([country.name for country in country_results])

        # Query languages
        language_results = CountryLanguage.objects.filter(language__icontains=search_text)[:5]
        suggestions.extend([list(set(language.language for language in language_results))])

    return JsonResponse(suggestions, safe=False)

def city_description(request):
    if request.method == 'POST':
        country = request.POST.get('country', 'NA')
        request.session['country_code'] = Country.objects.filter(name = country)[0].code
        return redirect(country_description)
    city = City.objects.filter(id = request.session.get('city_id'))[0]
    if city is not None:
        return render(request, 'city_description.html', {'city': city})
    return redirect(search)

def country_description(request):
    country = Country.objects.filter(code = request.session.get('country_code'))[0]
    if country is not None:
        capital = City.objects.filter(id = country.capital)[0]
        return render(request, 'country_description.html', {'country': country, 'capital': capital})
    return redirect(search)

def language_description(request):
    if request.method == 'POST':
        country = request.POST.get('country', 'NA')
        print(country)
        request.session['country_code'] = Country.objects.filter(name = country)[0].code
        return redirect(country_description)
    countryLanguages = CountryLanguage.objects.filter(id__in = request.session.get('lang_id'))
    language = countryLanguages[0].language
    if len(countryLanguages) > 0:
        return render(request, 'language_description.html', {'countryLanguages': countryLanguages, 'language': language})
    return redirect(search)