import sys

from constants import (
  SCORES,
  ALL_NEIGHBORS,
  LEN_TO_DIMS,
  SPLIT_ORDER,
)
from listings.add_word import add_word
from sum_choice_tree import (
  SumNode,
  bound,
  num_nodes,
)
from trie import make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]


def set_size(num_cells: int):
  global m, n, NEIGHBORS, ORDER
  m, n = LEN_TO_DIMS[num_cells]
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]
  ORDER = [0] * (m * n)
  for i, x in enumerate(SPLIT_ORDER[(m, n)]):
    ORDER[x] = m * n - i


ORDER = SPLIT_ORDER[(4, 4)]


# Listing 4: Building a tree
def build_tree(board_class, trie):
  root = SumNode()

  def choice_step(idx, trie, choices):
    letters = board_class[idx]
    for letter in letters:
      if trie.has_child(letter):
        choices.append((idx, letter))
        child = trie.child(letter)
        sum_step(idx, child, choices)
        choices.pop()

  def sum_step(idx, trie, choices):
    if trie.is_word():
      ordered_choices = sorted(
        choices, key=lambda c: -ORDER[c[0]]
      )
      score = SCORES[trie.length()]
      add_word(root, ordered_choices, score)
    for n_idx in NEIGHBORS[idx]:
      if n_idx not in (c[0] for c in choices):
        choice_step(n_idx, trie, choices)

  for i in range(m * n):
    choice_step(i, trie, [])
  return root


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  tree = build_tree(board_class, t)
  points = bound(tree)
  n_nodes = num_nodes(tree)
  sys.stderr.write(
    f"{board_class}: {points}, {n_nodes=}\n"
  )


if __name__ == "__main__":
  main()
