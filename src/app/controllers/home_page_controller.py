from requests import get
from json import loads
from datetime import datetime
from pytz import timezone


class HomePageController:
    def execute(self):

        ip_address = self.__get_ip_address()

        geo_location = self.__get_geo_location(ip_address)

        print(ip_address, flush=True)
        print(geo_location, flush=True)

        return {"ip_address": ip_address, **geo_location}

    def __get_geo_location(self, ip_address: str):
        try:
            response = get(f"http://ip-api.com/json/{ip_address}")
            data = response.json()

            current_timezone = timezone(data["timezone"])
            time = datetime.now(current_timezone).strftime("%H:%M")

            city = data["city"]
            state = data["regionName"]
            country = data["country"]

            address = f"{city}, {state} {country}"

            time_with_timezone = f"{current_timezone}: {time}"

            return {
                "isp": data["isp"],
                "latitude": data["lat"],
                "longitue": data["lon"],
                "address": address,
                "time": time_with_timezone,
            }
        except Exception as exception:
            raise exception

    def __get_ip_address(self):
        try:
            response = get("http://ip.seeip.org/jsonip?")
            data = loads(response.text)
            ip_address = data["ip"]
            return ip_address
        except Exception as exception:
            raise exception
