import sys

from constants import (
  SCORES,
  ALL_NEIGHBORS,
  LEN_TO_DIMS,
)
from trie import Trie, make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]


def set_size(num_cells: int):
  global m, n, NEIGHBORS
  m, n = LEN_TO_DIMS[num_cells]
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]


# Listing 3: sum bound on a Boggle board class
def sum_bound(
  board_class: list[str], trie: Trie
) -> int:
  used = {}

  def step(idx: int, node: Trie) -> int:
    score = 0
    used[idx] = True
    letters = board_class[idx]
    for letter in letters:  # new loop
      if node.has_child(letter):
        n = node.child(letter)
        if n.is_word() and not n.is_visited():
          score += SCORES[n.length()]
          n.set_visited()
        for n_idx in NEIGHBORS[idx]:
          if not used.get(n_idx):
            score += step(n_idx, n)
    used[idx] = False
    return score

  score = 0
  for i in range(m * n):
    score += step(i, trie)
  return score


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  points = sum_bound(board_class, t)
  print(f"{board_class}: {points}")


if __name__ == "__main__":
  main()
