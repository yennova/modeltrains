# === Stage 8: Сортировка записей ===
# Project: ModelTrains
from datetime import datetime


def _parse_date(value):
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    return value


def sort_by_name(records, reverse=False):
    return sorted(
        records,
        key=lambda rec: (rec.get("название") or "").lower(),
        reverse=reverse,
    )


def sort_by_date(records, reverse=False):
    return sorted(
        records,
        key=lambda rec: _parse_date(rec.get("дата_создания")),
        reverse=reverse,
    )


def sort_compositions(records, key="название", reverse=False):
    if key == "название":
        return sort_by_name(records, reverse=reverse)
    if key == "дата_создания":
        return sort_by_date(records, reverse=reverse)
    return sorted(records, key=lambda rec: rec.get(key), reverse=reverse)
