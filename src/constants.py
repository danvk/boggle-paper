#                  1, 2, 3, 4, 5, 6, 7,  8,     9..25
from typing import Sequence


SCORES = tuple(
  [0, 0, 0, 1, 1, 2, 3, 5, 11]
  + [11 for _ in range(9, 26)]
)
assert len(SCORES) == 26


def init_neighbors(w: int, h: int):
  def idx(x: int, y: int):
    return h * x + y

  def pos(idx: int):
    return (idx // h, idx % h)

  ns: list[list[int]] = []
  for i in range(0, w * h):
    x, y = pos(i)
    n = []
    for dx in range(-1, 2):
      nx = x + dx
      if nx < 0 or nx >= w:
        continue
      for dy in range(-1, 2):
        ny = y + dy
        if ny < 0 or ny >= h:
          continue
        if dx == 0 and dy == 0:
          continue
        n.append(idx(nx, ny))
    n.sort()
    ns.append(n)
  return ns


NEIGHBORS22 = init_neighbors(2, 2)
NEIGHBORS23 = init_neighbors(2, 3)
NEIGHBORS33 = init_neighbors(3, 3)
NEIGHBORS34 = init_neighbors(3, 4)
NEIGHBORS44 = init_neighbors(4, 4)
NEIGHBORS55 = init_neighbors(5, 5)

ALL_NEIGHBORS = {
  (2, 2): NEIGHBORS22,
  (2, 3): NEIGHBORS23,
  (3, 3): NEIGHBORS33,
  (3, 4): NEIGHBORS34,
  (4, 4): NEIGHBORS44,
  (5, 5): NEIGHBORS55,
}

LEN_TO_DIMS = {
  4: (2, 2),
  6: (2, 3),
  9: (3, 3),
  12: (3, 4),
  16: (4, 4),
  25: (5, 5),
}


SPLIT_ORDER_33 = (4, 5, 3, 1, 7, 0, 2, 6, 8)


def to_idx(x, y):
  return x * 4 + y


SPLIT_ORDER_34 = tuple(
  to_idx(x, y)
  for x, y in (
    (1, 1),
    (1, 2),  # middle
    (0, 1),
    (2, 1),
    (0, 2),
    (2, 2),  # middle sides
    (1, 0),
    (1, 3),  # top/bottom middle
    (0, 0),
    (2, 0),
    (0, 3),
    (2, 3),  # corners
  )
)
assert len(SPLIT_ORDER_34) == 12

SPLIT_ORDER_44 = tuple(
  to_idx(x, y)
  for x, y in (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),  # middle
    (0, 1),
    (3, 1),
    (0, 2),
    (3, 2),  # middle sides
    (1, 0),
    (1, 3),
    (2, 0),
    (2, 3),  # top/bottom middle
    (0, 0),
    (3, 0),
    (0, 3),
    (3, 3),  # corners
  )
)
assert len(SPLIT_ORDER_44) == 16
assert len(set(SPLIT_ORDER_44)) == 16

SPLIT_ORDER: dict[
  tuple[int, int], Sequence[int]
] = {
  (2, 2): (0, 1, 2, 3),
  (2, 3): (0, 1, 2, 3, 4, 5),
  (3, 3): SPLIT_ORDER_33,
  (3, 4): SPLIT_ORDER_34,
  (4, 4): SPLIT_ORDER_44,
}
