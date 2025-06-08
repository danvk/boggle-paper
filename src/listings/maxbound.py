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


# Listing 2: Calcluating max bound on a Boggle board class
def max_bound(
  bc: list[str], trie: Trie
) -> int:
  bound = 0
  for i in range(m * n):
    bound += max_bound_dfs(bc, i, trie, {})
  return bound


def max_bound_dfs(
  bc: list[str],
  idx: int,
  node: Trie,
  used,
) -> int:
  max_score = 0
  used[idx] = True
  letters = bc[idx]
  for letter in letters:
    if node.has_child(letter):
      letter_score = 0
      n = node.child(letter)
      if n.is_word():
        letter_score += SCORES[n.length()]
      for n_idx in NEIGHBORS[idx]:
        if not used.get(n_idx):
          letter_score += max_bound_dfs(
            bc, n_idx, n, used
          )
      max_score = max(max_score, letter_score)
  used[idx] = False
  return max_score


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  points = max_bound(board_class, t)
  print(f"{board_class}: {points}")


if __name__ == "__main__":
  main()
