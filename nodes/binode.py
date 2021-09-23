from dataclasses import dataclass
from typing import Union

from nodes.node import Node


@dataclass
class BiNode(Node):
    left: Union[Node, None] = None
    right: Union[Node, None] = None
