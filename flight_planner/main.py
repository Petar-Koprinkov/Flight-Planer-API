from services import CityService
from services import AirportService
from services import FlightService


def main():
    # Insert CRUD operations
    new_flight = {
        "flight_number": "BA250",
        "origin": "LHR",
        "destination": "DXB",
        "departure_time": "2024-12-10T15:00:00",
        "arrival_time": "2024-12-10T23:00:00"
    }

    FlightService.create_flight(new_flight)


if __name__ == "__main__":
    main()
