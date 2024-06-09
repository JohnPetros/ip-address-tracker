from requests import get
from json import loads
from datetime import datetime
from pytz import timezone
from re import search


class HomePageController:
    def execute(self, ip_address: str):
        try:
            if not ip_address:
                ip_address = self.__get_ip_address()

            is_valid_ip_address = self.__validate_ip_address(ip_address)
            if not is_valid_ip_address:
                raise Exception("Endereço IP inválido")

            print(is_valid_ip_address)
            geo_location = self.__get_geo_location(ip_address)

            return {"ip_address": ip_address, **geo_location}
        except Exception as exception:
            print("EITA")
            raise exception

    def __get_geo_location(self, ip_address: str):
        try:
            response = get(f"http://ip-api.com/json/{ip_address}")
            data = response.json()

            if data["status"] == "fail":
                raise Exception(
                    f"Erro ao buscar a geolocalização desse IP: {ip_address}"
                )

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

    def __validate_ip_address(self, ip_address):
        regex_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

        if search(regex_pattern, ip_address):
            return True
        else:
            return False

    def __get_ip_address(self):
        try:
            response = get("http://ip.seeip.org/jsonip?")
            data = loads(response.text)
            ip_address = data["ip"]
            return ip_address
        except Exception as exception:
            raise exception
