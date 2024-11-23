import json
import os
import general_functions

FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')

cities = {}
airports = {}
flights = {}


def load_data():
    global cities, airports, flights
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            cities = data.get('cities', {})
            airports = data.get('airports', {})
            flights = data.get('flights', {})


def save_data():
    data = {
        'cities': cities,
        'airports': airports,
        'flights': flights
    }
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


load_data()


# Functions for cities
def create_city(city):
    entity = general_functions.create_entity(cities, city)
    save_data()
    return entity


def get_all_cities():
    return print(list(cities.values()))


def get_city(city_id):
    return general_functions.get_entity(cities, city_id)


def delete_city(city_id):
    general_functions.delete_entity(cities, city_id)
    save_data()


def delete_all_cities():
    general_functions.delete_all_entities(cities)
    save_data()


# Functions for airports
def create_airport(airport):
    entity = general_functions.create_entity(airports, airport)
    save_data()
    return entity


def get_all_airports():
    return list(airports.values())


def get_airport(airport_id):
    return general_functions.get_entity(airports, airport_id)


def delete_airport(airport_id):
    general_functions.delete_entity(airports, airport_id)
    save_data()


def delete_all_airports():
    general_functions.delete_all_entities(airports)
    save_data()


def update_airport(airport_id, airport_data):
    entity = general_functions.update_entity(airports, airport_id, airport_data)
    save_data()
    return entity


def update_all_airports(airport_criteria):
    entities = general_functions.update_all_entities(airports, airport_criteria)
    save_data()
    return entities


# Functions for flights
def create_flight(flight):
    entity = general_functions.create_entity(flights, flight)
    save_data()
    return entity


def get_all_flights():
    return list(flights.values())


def get_flight(flight_id):
    return general_functions.get_entity(flights, flight_id)


def delete_flight(flight_id):
    general_functions.delete_entity(flights, flight_id)
    save_data()


def delete_all_flights():
    general_functions.delete_all_entities(flights)
    save_data()


def search_flight(criteria):
    return general_functions.search_entities(flights, criteria)


def update_flight(flight_id, flight_data):
    entity = general_functions.update_entity(flights, flight_id, flight_data)
    save_data()
    return entity





"""Creating city"""

# create_city({"name": "Los Angeles"})
# create_city({"name": "Nova Zagora"})


"""Creating airport"""

# create_airport({
#     "name": "JFK International Airport",
#     "location": "New York",
#     "code": "JFK"
# })
#
# create_airport({
#     "name": "JFK International Airport",
#     "location": "Nova Zagora",
#     "code": "JFRK"
# })


"""Creating flights"""

# create_flight({
#     "flight_number": "AA102",
#     "departure_airport": "JFK International Airport",
#     "arrival_airport": "San Francisco International Airport",
#     "departure_time": "2024-12-01 09:00",
#     "arrival_time": "2024-12-01 12:00",
#     "status": "Delayed"
# })
#
# create_flight({
#     "flight_number": "UA303",
#     "departure_airport": "Los Angeles International Airport",
#     "arrival_airport": "Chicago O'Hare International Airport",
#     "departure_time": "2024-12-01 07:30",
#     "arrival_time": "2024-12-01 13:00",
#     "status": "On Time"
# })
