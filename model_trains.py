# === Stage 1: Каркас модуля ===
# Project: ModelTrains
from dataclasses import dataclass


@dataclass
class Train:
    name: str
    scale: str
    wagons: int
    depot: str


def demo_trains() -> list[Train]:
    return [
        Train("Экспресс-1", "1:87", 12, "Депо-Север"),
        Train("Пассажирский-2", "1:90", 8, "Депо-Юг"),
        Train("Фрёт-3", "1:87", 20, "Депо-Центр"),
    ]


def main() -> None:
    trains = demo_trains()
    for train in trains:
        print(
            f"Состав: {train.name} | Масштаб: {train.scale} | "
            f"Вагонов: {train.wagons} | Депо: {train.depot}"
        )


if __name__ == "__main__":
    main()
