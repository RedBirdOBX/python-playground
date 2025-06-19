import requests

# https://www.weatherapi.com/
# http://api.weatherapi.com/v1/current.json?key={key}&q=Richmond&aqi=no

url = "http://api.weatherapi.com/v1/current.json?key=a475c101c9c842e79e6200917251706&q=Richmond&aqi=no"
response = requests.get(url)
json = response.json()

# {
#   "location": {
#     "name": "Richmond",
#     "region": "Virginia",
#     "country": "United States of America",
#     "lat": 37.5536,
#     "lon": -77.4606,
#     "tz_id": "America/New_York",
#     "localtime_epoch": 1750191760,
#     "localtime": "2025-06-17 16:22"
#   },
#   "current": {
#     "last_updated_epoch": 1750191300,
#     "last_updated": "2025-06-17 16:15",
#     "temp_c": 30.3,
#     "temp_f": 86.5,
#     "is_day": 1,
#     "condition": {
#       "text": "Partly cloudy",
#       "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#       "code": 1003
#     },
#     "wind_mph": 3.8,
#     "wind_kph": 6.1,
#     "wind_degree": 171,
#     "wind_dir": "S",
#     "pressure_mb": 1015,
#     "pressure_in": 29.96,
#     "precip_mm": 0,
#     "precip_in": 0,
#     "humidity": 61,
#     "cloud": 75,
#     "feelslike_c": 34.9,
#     "feelslike_f": 94.8,
#     "windchill_c": 30.3,
#     "windchill_f": 86.6,
#     "heatindex_c": 35.2,
#     "heatindex_f": 95.4,
#     "dewpoint_c": 23.7,
#     "dewpoint_f": 74.7,
#     "vis_km": 16,
#     "vis_miles": 9,
#     "uv": 4.6,
#     "gust_mph": 6,
#     "gust_kph": 9.7
#   }
# }


# expand on this technique
temp = json.get('current').get('temp_f')
print(temp)

