import numpy as np
from dataclasses import dataclass

@dataclass
class CellMap:
    grid: np.ndarray
    grid_width: int
    grid_height: int
    cell_size: int
    source_width: int
    source_height: int