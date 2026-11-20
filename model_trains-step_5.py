# === Stage 5: Связанная сущность ===
# Project: ModelTrains
import uuid


class Train:
    """Состав: название, масштаб, число вагонов и депо."""

    def __init__(self, name, scale, num_wagons, depot):
        self.name = name
        self.scale = scale
        self.num_wagons = num_wagons
        self.depot = depot

    def __repr__(self):
        return f"Train(name={self.name!r}, scale={self.scale}, num_wagons={self.num_wagons}, depot={self.depot!r})"


class Flight:
    """Рейс: привязка к составу по идентификатору и расписание."""

    def __init__(self, train_id, departure_time, arrival_time, stations):
        self.id = uuid.uuid4()
        self.train_id = train_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.stations = list(stations)

    def add_station(self, station):
        self.stations.append(station)

    def duration(self):
        return self.arrival_time - self.departure_time

    def __repr__(self):
        return (f"Flight(id={self.id}, train_id={self.train_id!r}, "
                f"departure={self.departure_time!r}, arrival={self.arrival_time!r}, "
                f"stations={self.stations})")


def add_flight(train_id, departure_time, arrival_time, stations, flights):
    flight = Flight(train_id, departure_time, arrival_time, stations)
    flights.append(flight)
    return flight


if __name__ == "__main__":
    trains = [Train("Экспресс", 1, 12, "Депо-1")]
    flights = []
    add_flight("Train-1", "10:00", "11:30", ["Москва", "Воронеж"], flights)
    print(flights)
