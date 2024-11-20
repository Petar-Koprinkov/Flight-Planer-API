from services import CityService


def main():
    new_city = {
        "name": "New York"
    }
    created_city = CityService.create_city(new_city)
    print("Created city:", created_city)

    another_city = {
        "name": "San Francisco"
    }
    created_city = CityService.create_city(another_city)
    print("Created city:", created_city)

    all_cities = CityService.get_all_cities()
    print("All cities:", all_cities)


if __name__ == "__main__":
    main()

