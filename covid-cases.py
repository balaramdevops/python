#!/usr/bin/env python3
from covid import Covid
covid = Covid(source="worldometers")
countries = covid.list_countries()
# print(countries)
cases = covid.get_status_by_country_name("usa")
for x in cases:
    print(x, ":", cases[x])






