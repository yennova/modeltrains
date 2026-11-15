# === Stage 3: Хранилище в памяти ===
# Project: ModelTrains
from __future__ import annotations


class TrainError(KeyError):
    """Ошибка доступа к составу по неизвестному идентификатору."""


class TrainStore:
    """Восстанавливаемое хранилище составов в памяти.

    Хранит составы в словаре, индексируя их по строковому идентификатору.
    Поддерживает добавление, получение по ключу и итерацию по всем записям.
    """

    def __init__(self) -> None:
        self._trains: dict[str, dict] = {}

    def add(self, train: dict) -> None:
        """Добавить состав, используя его идентификатор как ключ.

        Если состав с таким же идентификатором уже существует, его
        заменяют новым значением.
        """
        identifier = train["id"]
        self._trains[identifier] = dict(train)

    def get(self, identifier: str) -> dict:
        """Вернуть копию состава по идентификатору.

        Выбрасывает TrainError, если состав с указанным идентификатором
        не найден в хранилище.
        """
        return self._trains[identifier]

    def all(self) -> list[dict]:
        """Вернуть список всех составов в порядке добавления."""
        return list(self._trains.values())

    def __contains__(self, identifier: object) -> bool:
        return identifier in self._trains

    def __len__(self) -> int:
        return len(self._trains)


def load_trains(path: str) -> TrainStore:
    """Загрузить составы из JSON-файла в хранилище.

    Файл должен содержать список объектов с полями id, name, scale,
    cars, depot. Функция возвращает готовое к использованию хранилище.
    """
    import json

    store = TrainStore()
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    for item in data:
        store.add(item)
    return store


def dump_trains(store: TrainStore, path: str) -> None:
    """Сохранить содержимое хранилища в JSON-файл."""
    import json

    with open(path, "w", encoding="utf-8") as handle:
        json.dump(store.all(), handle, ensure_ascii=False, indent=2)
