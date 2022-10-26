""" Model for Chart """

from typing import List, Optional
from pydantic import BaseModel


# General Chart Model
class Item(BaseModel):
    i: str
    h: int
    w: int
    x: int
    y: int
    minW: int
    minH: int
    chartId: Optional[str]
    moved: Optional[bool]
    static: Optional[bool]

class Layouts(BaseModel):
  lg: List[Item]
  md: List[Item]
  sm: List[Item]

class DashboardModel(BaseModel):
  items: List[Item]
  layout: List[Item]
  layouts: Layouts
