import requests


def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Země nebyla nalezena.")
            return

        data = response.json()[0]

        name = data["name"]["common"]
        capital = data.get("capital", ["N/A"])[0]
        population = data["population"]
        region = data["region"]
        flag = data["flags"]["png"]

        print(f"\n🌍 Země: {name}")
        print(f"🏙️ Hlavní město: {capital}")
        print(f"👥 Populace: {population}")
        print(f"🌎 Region: {region}")
        print(f"🚩 Vlajka: {flag}")

    except Exception as e:
        print("Chyba:", e)


# hlavní program
if __name__ == "__main__":
    country = input("Zadej název země: ")
    get_country_info(country)