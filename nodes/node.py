from dataclasses import dataclass
from typing import Any

__all__ = ["Node"]


@dataclass
class Node:
    value: Any
