from dataclasses import dataclass
from typing import TypeVar, Union

from nodes.node import Node

BiNodeType = TypeVar("BiNodeType", bound="BiNode")


@dataclass
class BiNode(Node):
    left: Union[BiNodeType, None] = None
    right: Union[BiNodeType, None] = None
