from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the pygal 2-digit country code for the given country"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == "Yemen, Rep.":
            return "ye"
        elif country_name == "Vietnam":
            return "vn"
        elif country_name == "Venezuela, RB":
            return "ve"
    return None

