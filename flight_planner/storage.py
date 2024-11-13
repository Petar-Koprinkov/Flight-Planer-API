from general_functions import create_entity, get_entity, delete_entity, delete_all_entities

cities = {}
airports = {}
flights = {}


# Functions for cities
def create_city(city):
    return create_entity(cities, city)


def get_all_cities():
    return list(cities.values())


def get_city(city_id):
    return get_entity(cities, city_id)


def delete_city(city_id):
    delete_entity(cities, city_id)


def delete_all_cities():
    delete_all_entities(cities)


#Functions for airports
def create_airport(airport):
    return create_entity(airports, airport)


def get_all_airports():
    return list(airports.values())


def get_airport(airport_id):
    return get_entity(airports, airport_id)


def delete_airport(airport_id):
    delete_entity(airports, airport_id)


def delete_all_airports():
    delete_all_entities(airports)


#Functions for flights
def create_flight(flight):
    return create_entity(flights, flight)


def get_all_flights():
    return list(flights.values())


def get_flight(flight_id):
    return get_entity(flights, flight_id)


def delete_flight(flight_id):
    delete_entity(flights, flight_id)


def delete_all_flights():
    delete_all_entities(flights)
