# --- entities.py ---
from dataclasses import dataclass

@dataclass
class UserEntity:
    id: int
    email: str
    is_active: bool = True