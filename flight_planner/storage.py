import general_functions

cities = {}
airports = {}
flights = {}


# Functions for cities
def create_city(city):
    return general_functions.create_entity(cities, city)


def get_all_cities():
    return list(cities.values())


def get_city(city_id):
    return general_functions.get_entity(cities, city_id)


def delete_city(city_id):
    general_functions.delete_entity(cities, city_id)


def delete_all_cities():
    general_functions.delete_all_entities(cities)


#Functions for airports
def create_airport(airport):
    return general_functions.create_entity(airports, airport)


def get_all_airports():
    return list(airports.values())


def get_airport(airport_id):
    return general_functions.get_entity(airports, airport_id)


def delete_airport(airport_id):
    general_functions.delete_entity(airports, airport_id)


def delete_all_airports():
    general_functions.delete_all_entities(airports)


def update_airport(airport, airport_id, airport_data):
    return general_functions.update_entity(airport, airport_id, airport_data)


#Functions for flights
def create_flight(flight):
    return general_functions.create_entity(flights, flight)


def get_all_flights():
    return list(flights.values())


def get_flight(flight_id):
    return general_functions.get_entity(flights, flight_id)


def delete_flight(flight_id):
    general_functions.delete_entity(flights, flight_id)


def delete_all_flights():
    general_functions.delete_all_entities(flights)


def search_flight(flights, criteria):
    return general_functions.search_entities(flights, criteria)


def update_flight(flight, flight_id, flight_data):
    return general_functions.update_entity(flight, flight_id, flight_data)
