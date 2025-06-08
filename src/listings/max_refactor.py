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


# Listing 5: max bound with two functions
def max_bound(
  board_class: list[str], trie: Trie
) -> int:
  used = {}

  def choice_step(idx, node):
    score = 0
    used[idx] = True
    letters = board_class[idx]
    for letter in letters:
      if node.has_child(letter):
        child = node.child(letter)
        score = max(
          score,
          sum_step(idx, child),
        )
    used[idx] = False
    return score

  def sum_step(idx, node):
    score = 0
    if node.is_word():
      score += SCORES[node.length()]
    for n_idx in NEIGHBORS[idx]:
      if not used.get(n_idx):
        score += choice_step(n_idx, node)
    return score

  bound = 0
  for i in range(m * n):
    bound += choice_step(i, trie)
  return bound


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  points = max_bound(board_class, t)
  print(f"{board_class}: {points}")


if __name__ == "__main__":
  main()
