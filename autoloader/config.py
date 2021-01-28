from typing import List
from enum import Enum, auto
from dataclasses import dataclass


class DriverFlavour(Enum):
    Firefox = auto()
    Chrome = auto()


@dataclass(frozen=True)
class Config:
    driver_flavour: DriverFlavour
    target_url: str
    target_files: str
    driver_path: str = None
