import requests


def get_country_data(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()[0]


def get_population(country):

    data = get_country_data(country)

    if not data:
        return "Country not found"

    population = data["population"]

    return f"Population of {country.title()} is {population}"


def get_capital(country):

    data = get_country_data(country)

    if not data:
        return "Country not found"

    capital = data["capital"][0]

    return f"Capital of {country.title()} is {capital}"


def get_currency(country):

    data = get_country_data(country)

    if not data:
        return "Country not found"

    currencies = data["currencies"]

    currency_code = list(currencies.keys())[0]

    currency_name = currencies[currency_code]["name"]

    return (
        f"Currency of {country.title()} is "
        f"{currency_name} ({currency_code})"
    )