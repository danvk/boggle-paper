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
  to_dot,
)
from trie import make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]


def set_size(num_cells: int):
  global m, n, NEIGHBORS
  m, n = LEN_TO_DIMS[num_cells]
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]


type char = str

Path = list[(int, char)]


def find(xs, fn):
  for x in xs:
    if fn(x):
      return x
  return None


# Listing 3: add_word to sum/choice tree
def add_word(
  node: SumNode, path: Path, points: int
):
  if len(path) == 0:
    node.points += points
    return node

  cell, letter = path[0]
  choice_n = find(
    node.children, lambda c: c.cell == cell
  )
  if not choice_n:
    choice_n = ChoiceNode(cell=cell)
    node.children.append(choice_n)

  sum_n = choice_n.children.get(letter)
  if not sum_n:
    sum_n = SumNode()
    choice_n.children[letter] = sum_n

  return add_word(sum_n, path[1:], points)


# /Listing


def build_tree_alt(board_class, trie):
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
    score = SCORES[trie_node.length()]
    add_word(root, choices, score)
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


def main():
  t = make_trie("wordlists/enable2k.txt")
  board_class = sys.argv[1:]
  set_size(len(board_class))
  tree = build_tree_alt(board_class, t)
  points = bound(tree)
  sys.stderr.write(f"{board_class}: {points}\n")
  print(to_dot(tree, board_class))
  # poetry run python -m paper.3b_max_tree lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz
  # ['lnrsy', 'chkmpt', 'lnrsy', 'aeiou', 'aeiou', 'aeiou', 'chkmpt', 'lnrsy', 'bdfgjqvwxz']: 9460


if __name__ == "__main__":
  main()
