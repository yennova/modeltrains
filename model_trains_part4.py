# === Stage 4: Удаление и восстановление ===
# Project: ModelTrains
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


@dataclass
class SoftDeletedTrain:
    """Состав, помеченный как удалённый, но сохраняющий все данные для восстановления."""

    train_id: str
    name: str
    scale: str
    wagons: int
    depot: str
    deleted_at: Optional[datetime] = None
    is_deleted: bool = True
    restore_count: int = 0


class TrainRegistry:
    """Регистр составов с поддержкой мягкого удаления и восстановления."""

    def __init__(self):
        self._trains: Dict[str, dict] = {}

    def add_train(self, name: str, scale: str, wagons: int, depot: str) -> str:
        train_id = f"T{len(self._trains) + 1:04d}"
        self._trains[train_id] = {
            "train_id": train_id,
            "name": name,
            "scale": scale,
            "wagons": wagons,
            "depot": depot,
            "deleted_at": None,
            "is_deleted": False,
            "restore_count": 0,
        }
        return train_id

    def delete_train(self, train_id: str) -> Optional[SoftDeletedTrain]:
        train = self._trains.get(train_id)
        if train is None or train["is_deleted"]:
            return None
        train["is_deleted"] = True
        train["deleted_at"] = datetime.now()
        return SoftDeletedTrain(
            train_id=train["train_id"],
            name=train["name"],
            scale=train["scale"],
            wagons=train["wagons"],
            depot=train["depot"],
            deleted_at=train["deleted_at"],
            is_deleted=True,
            restore_count=0,
        )

    def restore_train(self, train_id: str) -> bool:
        train = self._trains.get(train_id)
        if train is None or not train["is_deleted"]:
            return False
        train["is_deleted"] = False
        train["deleted_at"] = None
        train["restore_count"] += 1
        return True

    def list_active_trains(self) -> list:
        return [
            t for t in self._trains.values() if not t["is_deleted"]
        ]

    def list_deleted_trains(self) -> list:
        return [
            t for t in self._trains.values() if t["is_deleted"]
        ]

    def get_train(self, train_id: str) -> Optional[dict]:
        return self._trains.get(train_id)
