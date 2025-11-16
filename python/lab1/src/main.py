from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

@dataclass
class PascalTriangle:
    rows: int
    _data: List[List[int]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if not isinstance(self.rows, int):
            raise TypeError("rows must be an integer")
        if self.rows < 0:
            raise ValueError("rows must be a positive integer")
        self._data = self._generate()
    
    def _generate(self) -> List[List[int]]:
        triangle: List[List[int]] = []

        for i in range(self.rows):
            if i == 0:
                triangle.append([1])
                continue
            prevRow = triangle[-1]
            newRow: List[int] = [1]

            for j in range(len(prevRow) - 1):
                newRow.append(prevRow[j] + prevRow[j + 1])
            newRow.append(1)
            triangle.append(newRow)
        
        return triangle
    
    @property
    def data(self) -> List[List[int]]:
        return [row.copy() for row in self.data]
    
    def __str__(self) -> str:
        strRows = [" ".join(str(i) for i in row) for row in self._data]
        if not strRows:
            return ""
        
        maxWidth = len(strRows[-1])
        return "\n".join(row.center(maxWidth) for row in strRows)

def readPositiveInt(promt: str = "Enter a postive integer n: "):
    while True:
        raw = input(promt).strip()

        if not raw.isdigit():
            print("Error: please enter a postive integer")
            continue
        
        val = int(raw)
        if val < 0:
            print("Error: the number must be greater than zero")
            continue

        return val

def main() -> None:
    n = readPositiveInt()
    triangle = PascalTriangle(n)
    print(triangle)

if __name__ == "__main__":
    main()
