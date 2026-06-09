from tools import (
    get_population,
    get_capital,
    get_currency
)


def run_agent(query):

    query = query.lower()

    if "population of" in query:

        country = query.replace(
            "population of",
            ""
        ).strip()

        return get_population(country)

    elif "capital of" in query:

        country = query.replace(
            "capital of",
            ""
        ).strip()

        return get_capital(country)

    elif "currency of" in query:

        country = query.replace(
            "currency of",
            ""
        ).strip()

        return get_currency(country)

    return (
        "Ask about population, "
        "capital or currency."
    )