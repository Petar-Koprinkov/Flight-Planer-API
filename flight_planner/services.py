import storage
from typing import Callable, Union


class CityService:
    @staticmethod
    def create_city(city: str) -> Callable:
        return storage.create_city(city)

    @staticmethod
    def get_all_cities() -> Callable:
        return storage.get_all_cities()

    @staticmethod
    def get_city(city_id: int) -> Union[str, Exception]:
        city = storage.get_city(city_id)
        if city is None:
            raise KeyError(f"City with id {city_id} not found!")
        return city

    @staticmethod
    def delete_city(city_id: int) -> None:
        storage.delete_city(city_id)
        return ''

    @staticmethod
    def delete_all_cities() -> None:
        storage.delete_all_cities()
        return ''


class AirportService:
    @staticmethod
    def create_airport(airport: str) -> Callable:
        return storage.create_airport(airport)

    @staticmethod
    def get_all_airports():
        return storage.get_all_airports()

    @staticmethod
    def get_airport(airport_id: int) -> Union[str, Exception]:
        airport = storage.get_airport(airport_id)
        if airport is None:
            raise KeyError(f"Airport with id {airport_id} not found!")
        return airport

    @staticmethod
    def delete_airport(airport_id: int) -> None:
        storage.delete_airport(airport_id)
        return ''

    @staticmethod
    def delete_all_airports() -> None:
        storage.delete_all_airports()
        return ''

    @staticmethod
    def update_airport(airport: str, airport_id: int, airport_data: str) -> Callable:
        return storage.update_flight(airport, airport_id, airport_data)

    @staticmethod
    def update_all_airports(airport: str, airport_criteria: str) -> Callable:
        return storage.update_all_airports(airport, airport_criteria)


class FlightService:

    @staticmethod
    def create_flight(flight: str) -> Callable:
        return storage.create_flight(flight)

    @staticmethod
    def get_all_flights() -> Callable:
        return storage.get_all_flights()

    @staticmethod
    def get_flight(flight_id: int) -> Union[str, Exception]:
        flight = storage.get_flight(flight_id)
        if flight is None:
            raise KeyError(f"Flight with id {flight_id} not found!")
        return flight

    @staticmethod
    def delete_flight(flight_id: int) -> None:
        storage.delete_flight(flight_id)
        return ''

    @staticmethod
    def delete_all_flights() -> None:
        storage.delete_all_flights()
        return ''

    @staticmethod
    def search_flights(flights: str, flight_criteria: str) -> Callable:
        return storage.search_flight(flights, flight_criteria)

    @staticmethod
    def update_flight(flight: str, flight_id: int, flight_data: str) -> Callable:
        return storage.update_flight(flight, flight_id, flight_data)
