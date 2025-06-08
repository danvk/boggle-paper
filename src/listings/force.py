import sys

from constants import (
  SCORES,
  ALL_NEIGHBORS,
  LEN_TO_DIMS,
)
from trie import make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]


def set_size(num_cells: int):
  global m, n, NEIGHBORS
  m, n = LEN_TO_DIMS[num_cells]
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]


# Listing 6: Build+Force operation on Tree
def forced_tree(
  board_class: list[str], board: str, trie
):
  used = {}

  def choice_step(idx, trie):
    score = 0
    used[idx] = True
    letter = board[idx]
    if trie.has_child(letter):
      n = trie.child(letter)
      score = sum_step(idx, n)
    used[idx] = False
    return score

  def sum_step(idx, trie):
    score = 0
    if trie.is_word():
      score += SCORES[trie.length()]
    for n_idx in NEIGHBORS[idx]:
      if not used.get(n_idx):
        score += choice_step(n_idx, trie)
    return score

  bound = 0
  for i in range(m * n):
    bound += choice_step(i, trie)
  return bound


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board, *board_class = sys.argv[1:]
  set_size(len(board_class))
  points = forced_tree(board_class, board, t)
  print(f"{board_class} -> {board}: {points}")
  # poetry run python -m paper.4_force aceh x
  # ['x'] -> aceh: 4
  # poetry run python -m paper.4_force beef x
  # ['x'] -> beef: 6
  # poetry run python -m paper.4_force eebfee x
  # ['x'] -> eebfee: 12


if __name__ == "__main__":
  main()
