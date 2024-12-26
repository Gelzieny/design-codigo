from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
  respose = elem1 + elem2

  return {'sum': respose}

val1 = add(2, 4.67)

print(val1)