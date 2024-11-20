import storage


class CityService:
    @staticmethod
    def create_city(city):
        return storage.create_city(city)

    @staticmethod
    def get_all_cities():
        return storage.get_all_cities()

    @staticmethod
    def get_city(city_id):
        city = storage.get_city(city_id)
        if city is None:
            raise KeyError(f"City with id {city_id} not found!")
        return city

    @staticmethod
    def delete_city(city_id):
        storage.delete_city(city_id)
        return ''

    @staticmethod
    def delete_all_cities():
        storage.delete_all_cities()
        return ''


class AirportService:
    @staticmethod
    def create_airport(airport):
        return storage.create_airport(airport)

    @staticmethod
    def get_all_airports():
        return storage.get_all_airports()

    @staticmethod
    def get_airport(airport_id):
        airport = storage.get_airport(airport_id)
        if airport is None:
            raise KeyError(f"Airport with id {airport_id} not found!")
        return airport

    @staticmethod
    def delete_airport(airport_id):
        storage.delete_airport(airport_id)
        return ''

    @staticmethod
    def delete_all_airports():
        storage.delete_all_airports()
        return ''

    @staticmethod
    def update_airport(airport_id, airport_data):
        return storage.update_airport(airport_id, airport_data)

    @staticmethod
    def update_all_airports(airport_criteria):
        return storage.update_all_airports(airport_criteria)


class FlightService:
    @staticmethod
    def create_flight(flight):
        return storage.create_flight(flight)

    @staticmethod
    def get_all_flights():
        return storage.get_all_flights()

    @staticmethod
    def get_flight(flight_id):
        flight = storage.get_flight(flight_id)
        if flight is None:
            raise KeyError(f"Flight with id {flight_id} not found!")
        return flight

    @staticmethod
    def delete_flight(flight_id):
        storage.delete_flight(flight_id)
        return ''

    @staticmethod
    def delete_all_flights():
        storage.delete_all_flights()
        return ''

    @staticmethod
    def search_flights(criteria):
        return storage.search_flight(criteria)

    @staticmethod
    def update_flight(flight_id, flight_data):
        return storage.update_flight(flight_id, flight_data)
