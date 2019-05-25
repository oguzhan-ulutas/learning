import json

import pygal

from country_codes_0 import get_country_code

# Load the data into a list
filename = "gdp_json.json"
with open(filename) as f:
    gdp_data = json.load(f)
    # Build a dictionary of gdp
    countries_gdp = {}
    for gdp_dict in gdp_data:
        if gdp_dict["Year"] == 2016:
            country_name = gdp_dict["Country Name"]
            gdp = int(float(gdp_dict["Value"]))
            code = get_country_code(country_name)
            if code:
                countries_gdp[code] = round(gdp/1000000000)
            else:
                print("Error " + country_name)


wm = pygal.maps.world.World()

wm.title = "World GDP in 2016 in Billion USD, by Country"
wm.add("GDP", countries_gdp)
wm.render_to_file("world_gdp_2016.svg")
