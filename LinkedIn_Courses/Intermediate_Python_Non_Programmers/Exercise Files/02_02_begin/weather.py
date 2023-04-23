# api key b8a6b89790729368d97631c6e6b3418a
# falls church va lat 38.883930 long -77.173698
# OpenWeather api call https://api.openweathermap.org/data/2.5/weather?lat=38.883930&lon=-77.173698&appid=b8a6b89790729368d97631c6e6b3418a
#  make sure to pip install requests first

import requests

# try:
#     # adding "units=metric" after weather? to show weather in celsisu/farenheit
#     response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=38.883930&lon=-77.173698&appid=b8a6b89790729368d97631c6e6b3418a")

# except:
#     print("No internet access")

# response_json = response.json()

# temp = response_json["main"]["temp"]
# temp_min = response_json["main"]["temp_min"]
# temp_max = response_json["main"]["temp_max"]

# print(f"In Falls Church VA, it is currentl {temp}° Celsius")
# print(f"Today's high: {temp_max}° celsius")
# print(f"Today's Low: {temp_min}° celcius")

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            # adding "units=metric" after weather? to show weather in celsisus; "imperial" for farenheit
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=b8a6b89790729368d97631c6e6b3418a")

        except:
            print("No internet access")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units =="imperial":
            units_symbol = "F"
        print(f"In {self.name}, it is currently {self.temp}° {units_symbol}")
        print(f"Today's high: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")
        print( "\n")


my_city = City("Falls Church VA", 38.883930, -77.173698, units="imperial")
my_city.temp_print()

vacation_city = City("Portland", 45.5152, -122.6768, units="imperial")
vacation_city.temp_print()

seoul_city = City("Seoul S Korea", 37.566536, 126.977966)
seoul_city.temp_print()

# print(vacation_city.response_json)