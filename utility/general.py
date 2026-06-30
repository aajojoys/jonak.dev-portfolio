import requests, geoip2.database
from django.conf import settings

IPAPI_URL = "https://ipapi.co"
IPWHOIS_URL = "https://ipwho.is"
WIREGUARD_IP = "10.100.0.1"
LOCALHOST_IP = "127.0.0.1"
GEOLITE2_CITY_PATH = "others/GeoLite2-City.mmdb"

reader = geoip2.database.Reader(f"{settings.BASE_DIR}/{GEOLITE2_CITY_PATH}")

def get_client_ip(request):
    xff = request.META.get("HTTP_X_FORWARDED_FOR")

    if xff: return xff.split(",")[0].strip()

    return request.META.get("REMOTE_ADDR")

def get_ip_info(ip_addr):
    res = requests.get(f"{IPAPI_URL}/{ip_addr}/json/")
    if res.status_code == requests.codes.ok:
        return { "success": True, **res.json() }
    else:
        res = requests.get(f"{IPWHOIS_URL}/{ip_addr}")
        if res.status_code == requests.codes.ok:
            return { "success": True, **res.json() }
        else:
            response = reader.city(ip_addr)
        return dict(ip=ip_addr, country=response.country.name, city=response.city.name, latitude=response.location.latitude, longitude=response.location.longitude, success=False)

def is_localhost(ip_addr):
    return ip_addr in [LOCALHOST_IP, WIREGUARD_IP]
