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


# Listing 4: max bound on a Boggle board class
def max_bound(
  board_class: list[str], trie: Trie
) -> int:
  used = {}

  def step(idx: int, node: Trie) -> int:
    score = 0
    used[idx] = True
    letters = board_class[idx]
    for letter in letters:
      if node.has_child(letter):
        letter_score = 0
        n = node.child(letter)
        if n.is_word():
          letter_score += SCORES[n.length()]
        for n_idx in NEIGHBORS[idx]:
          if not used.get(n_idx):
            letter_score += step(n_idx, n)
        score = max(score, letter_score)
    used[idx] = False
    return score

  bound = 0
  for i in range(m * n):
    bound += step(i, trie)
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
