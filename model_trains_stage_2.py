# === Stage 2: Проверка полей ===
# Project: ModelTrains
import re

def normalize_train_name(name):
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    return name.title()


def normalize_scale(scale):
    scale = scale.strip()
    if not scale:
        return ""
    match = re.match(r"^(\d+(?:\.\d+)?)\s*(mm|cm|inch|in|mm)$", scale, re.IGNORECASE)
    if not match:
        return ""
    value = float(match.group(1))
    unit = match.group(2).lower()
    return f"{value:g} {unit}"


def normalize_cars(cars):
    try:
        cars = int(cars)
    except (TypeError, ValueError):
        return 0
    if cars < 0:
        return 0
    return cars


def normalize_depot(depot):
    depot = depot.strip()
    depot = re.sub(r"\s+", " ", depot)
    return depot


def validate_train(train):
    errors = []

    name = normalize_train_name(train.get("name", ""))
    if not name:
        errors.append("Название состава обязательно для заполнения.")
    else:
        if len(name) > 100:
            errors.append("Название состава не должно превышать 100 символов.")

    scale = normalize_scale(train.get("scale", ""))
    if not scale:
        errors.append("Укажите масштаб в формате число и единица измерения, например 1:87 или 87 mm.")
    elif scale not in ("", "87 mm", "87 cm", "1:87", "1:88", "1:900", "1:76"):
        errors.append("Неверный формат масштаба. Примеры: 87 mm, 1:87, 1:900.")

    cars = normalize_cars(train.get("cars", 0))
    if cars < 0:
        errors.append("Число вагонов не может быть отрицательным.")
    elif cars > 1000:
        errors.append("Число вагонов не должно превышать 1000.")

    depot = normalize_depot(train.get("depot", ""))
    if not depot:
        errors.append("Укажите название депо.")
    elif len(depot) > 100:
        errors.append("Название депо не должно превышать 100 символов.")

    return {
        "name": name,
        "scale": scale,
        "cars": cars,
        "depot": depot,
        "errors": errors,
    }
