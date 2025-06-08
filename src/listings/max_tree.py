import sys

from constants import (
  SCORES,
  ALL_NEIGHBORS,
  LEN_TO_DIMS,
)
from sum_choice_tree import (
  ChoiceNode,
  SumNode,
  bound,
  num_nodes,
  to_dot,
)
from trie import Trie, make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]


def set_size(num_cells: int):
  global m, n, NEIGHBORS
  m, n = LEN_TO_DIMS[num_cells]
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]


# Listing 5b: Calculating max bound with a tree
def build_tree(
  board_class: str, trie: Trie
) -> SumNode:
  used = {}

  def choice_step(idx, trie) -> ChoiceNode:
    node = ChoiceNode(cell=idx)
    used[idx] = True
    letters = board_class[idx]
    for letter in letters:
      if trie.has_child(letter):
        n = sum_step(idx, trie.child(letter))
        if bound(n):
          node.children[letter] = n
    used[idx] = False
    return node

  def sum_step(idx, trie) -> SumNode:
    node = SumNode(points=0)
    if trie.is_word():
      node.points = SCORES[trie.length()]
      node.trie_node = trie  # HIDE
    for n_idx in NEIGHBORS[idx]:
      if not used.get(n_idx):
        n = choice_step(n_idx, trie)
        if bound(n):  # HIDE
          node.children.append(n)
    return node

  root = SumNode(points=0)
  root.children = [
    choice_step(i, trie) for i in range(m * n)
  ]
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
  print(to_dot(tree, board_class))
  # poetry run python -m paper.3b_max_tree lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz
  # ['lnrsy', 'chkmpt', 'lnrsy', 'aeiou', 'aeiou', 'aeiou', 'chkmpt', 'lnrsy', 'bdfgjqvwxz']: 9460


if __name__ == "__main__":
  main()
