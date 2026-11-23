# === Stage 6: Генерация идентификаторов ===
# Project: ModelTrains
PROJECT_PREFIX = "MTR"


def generate_unique_id(entity_name):
    counter = {entity_name: 0}
    while True:
        counter[entity_name] += 1
        candidate = f"{PROJECT_PREFIX}_{entity_name}_{counter[entity_name]}"
        if candidate not in _USED_IDS:
            _USED_IDS.add(candidate)
            return candidate


_USED_IDS = set()


def reset_id_generator():
    _USED_IDS.clear()
