import requests
from colorama import Fore
from bs4 import BeautifulSoup


class Wether:
    def __init__(self):
        url = "https://yandex.ru/pogoda/ru/moscow?lat=55.755863&lon=37.6177"
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            weather_container_operator = soup.find(
                "span",
                class_="AppFactTemperature_sign__1MeN4 AppFactTemperature_attr__8pcxc",
            )
            weather_container = soup.find(
                "span", class_="AppFactTemperature_value__2qhsG"
            )
            if weather_container:
                op_temp = weather_container_operator
                temp = weather_container  # .find("temperature-value")
                print(
                    Fore.GREEN
                    + f"Temperature in Moscow now: {op_temp.text}{temp.text} °C"
                )
        else:
            print(Fore.RED + f"Ошибка доступа: {response.status_code}")


if __name__ == "__main__":
    Wether()
