#!/usr/bin/env python3
from covid import Covid
import sys

class Covidcases():
    def cases_bycountry(self, country):
        covid = Covid(source="worldometers")
        countries = covid.list_countries()
        # print(countries)
        cases = covid.get_status_by_country_name(country)
        for x in cases:
            print(x, ":", cases[x])

if __name__ == "__main__":
    cases = Covidcases()
    cases.cases_bycountry(*sys.argv[1:])






