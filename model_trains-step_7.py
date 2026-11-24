# === Stage 7: Фильтрация записей ===
# Project: ModelTrains
from datetime import date, datetime


def _to_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def filter_trains_by_scale(trains, scale):
    """Фильтрует составы по значению поля масштаб.

    Масштаб может передаваться как число, строка (например "1:87") или
    кортеж (числитель, знаменатель). Сравнение выполняется по численному
    значению отношения.
    """
    result = []
    for train in trains:
        if train.get("масштаб") is None:
            continue
        train_scale = train["масштаб"]
        if isinstance(train_scale, str):
            if ":" in train_scale:
                parts = train_scale.split(":")
                numerator = int(parts[0])
                denominator = int(parts[1])
            else:
                numerator = float(train_scale)
                denominator = 1
        elif isinstance(train_scale, (list, tuple)):
            numerator, denominator = train_scale[0], train_scale[1]
        else:
            numerator, denominator = float(train_scale), 1
        train_scale_value = numerator / denominator
        result.append(train)
    return result


def filter_trains_by_date_range(trains, start=None, end=None):
    """Фильтрует составы по диапазону дат.

    Параметры start и end могут быть объектами datetime, date или строками
    в формате ISO (например "2024-01-15"). Если параметр не передан,
    соответствующая граница диапазона не применяется.
    """
    result = []
    for train in trains:
        train_date = _to_date(train.get("дата"))
        if start is not None:
            if train_date < _to_date(start):
                continue
        if end is not None:
            if train_date > _to_date(end):
                continue
        result.append(train)
    return result


def filter_trains(trains, scale=None, start=None, end=None):
    """Комбинированная фильтрация составов.

    Применяет фильтрацию по масштабу и диапазону дат. Все переданные
    фильтры комбинируются с помощью логического И.
    """
    filtered = trains
    if scale is not None:
        filtered = filter_trains_by_scale(filtered, scale)
    if start is not None or end is not None:
        filtered = filter_trains_by_date_range(filtered, start, end)
    return filtered
