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


# Listing 8: Building an orderly tree
def build_orderly_tree(board_class, trie):
  root = SumNode()
  for i in range(m * n):
    choice_step(board_class, i, trie, [], root)
  return root


def choice_step(
  board_class, idx, trie_node, choices, root
):
  letters = board_class[idx]
  for letter in letters:
    if trie_node.has_child(letter):
      choices.append((idx, letter))
      sum_step(
        board_class,
        idx,
        trie_node.child(letter),
        choices,
        root,
      )
      choices.pop()


def sum_step(
  board_class, idx, trie_node, choices, root
):
  if trie_node.is_word():
    ordered_choices = sorted(
      choices, key=lambda c: -ORDER[c[0]]
    )
    score = SCORES[trie_node.length()]
    add_word(root, ordered_choices, score)
  for n_idx in NEIGHBORS[idx]:
    if n_idx not in (
      cell for cell, _letter in choices
    ):
      choice_step(
        board_class,
        n_idx,
        trie_node,
        choices,
        root,
      )


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  tree = build_orderly_tree(board_class, t)
  points = bound(tree)
  n_nodes = num_nodes(tree)
  sys.stderr.write(
    f"{board_class}: {points}, {n_nodes=}\n"
  )


if __name__ == "__main__":
  main()
