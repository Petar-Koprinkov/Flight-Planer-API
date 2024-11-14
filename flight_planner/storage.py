from typing import Callable, Dict, List

import general_functions

cities = {}
airports = {}
flights = {}


# Functions for cities
def create_city(city: str) -> Dict:
    return general_functions.create_entity(cities, city)


def get_all_cities() -> List:
    return list(cities.values())


def get_city(city_id) -> str:
    return general_functions.get_entity(cities, city_id)


def delete_city(city_id) -> None:
    general_functions.delete_entity(cities, city_id)


def delete_all_cities() -> None:
    general_functions.delete_all_entities(cities)


#Functions for airports
def create_airport(airport) -> Dict:
    return general_functions.create_entity(airports, airport)


def get_all_airports() -> List:
    return list(airports.values())


def get_airport(airport_id) -> str:
    return general_functions.get_entity(airports, airport_id)


def delete_airport(airport_id) -> None:
    general_functions.delete_entity(airports, airport_id)


def delete_all_airports() -> None:
    general_functions.delete_all_entities(airports)


def update_airport(airport, airport_id, airport_data) -> Dict:
    return general_functions.update_entity(airport, airport_id, airport_data)


def update_all_airports(airports, criteria) -> Dict:
    return general_functions.update_all_entities(airports, criteria)


#Functions for flights
def create_flight(flight) -> Dict:
    return general_functions.create_entity(flights, flight)


def get_all_flights() -> List:
    return list(flights.values())


def get_flight(flight_id) -> str:
    return general_functions.get_entity(flights, flight_id)


def delete_flight(flight_id) -> None:
    general_functions.delete_entity(flights, flight_id)


def delete_all_flights() -> None:
    general_functions.delete_all_entities(flights)


def search_flight(flights, criteria) -> str:
    return general_functions.search_entities(flights, criteria)


def update_flight(flight, flight_id, flight_data) -> Dict:
    return general_functions.update_entity(flight, flight_id, flight_data)
