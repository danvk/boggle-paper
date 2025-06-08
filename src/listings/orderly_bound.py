import sys

from constants import (
  ALL_NEIGHBORS,
  LEN_TO_DIMS,
  SPLIT_ORDER,
)
from listings.orderly import (
  build_orderly_tree,
  set_size as orderly_set_size,
)
from sum_choice_tree import (
  ChoiceNode,
  SumNode,
  bound,
  num_nodes,
)
from trie import make_trie

m = 4
n = 4
N = m * n
NEIGHBORS = ALL_NEIGHBORS[(m, n)]
ORDER = SPLIT_ORDER[(4, 4)]


def set_size(num_cells: int):
  global N, m, n, NEIGHBORS, ORDER, CELL_ORDER
  m, n = LEN_TO_DIMS[num_cells]
  N = m * n
  NEIGHBORS = ALL_NEIGHBORS[(m, n)]
  ORDER = [0] * (m * n)
  CELL_ORDER = SPLIT_ORDER[(m, n)]
  for i, x in enumerate(SPLIT_ORDER[(m, n)]):
    ORDER[x] = m * n - i
  orderly_set_size(num_cells)


type char = str

candidates = []


def clear_candidates():
  candidates.clear()


def get_candidates():
  return candidates


def record_candidate_board(
  choices: list[char], bound: int
):
  cells = [""] * N
  for cell, choice in zip(
    SPLIT_ORDER[(m, n)], choices
  ):
    cells[cell] = choice
  bd = "".join(cells)
  candidates.append((bound, bd))
  print(f"{bound} {bd}")


# Listing 11: orderly_bound
# Assumes N >= 1
def orderly_bound(
  root: SumNode,  # Orderly(N)
  board_class: list[str],
  S_high: int,
):
  def step(
    points: int,
    idx: int,
    # letters chosen on previous cells
    choices: list[char],
    stack: list[ChoiceNode],
  ):
    b = points + sum(bound(n) for n in stack)
    if b < S_high:
      return  # This path is eliminated
    if idx == N:
      # complete board that can't be eliminated
      record_candidate_board(choices, b)
      return

    # Try each letter on the next cell in order.
    cell = CELL_ORDER[idx]
    for letter in board_class[cell]:
      next_nodes = [
        n for n in stack if n.cell == cell
      ]
      next_stack = [
        n for n in stack if n.cell != cell
      ]
      next_points = points
      next_choices = choices + [letter]
      for node in next_nodes:
        letter_node = node.children.get(letter)
        if letter_node:
          next_stack += letter_node.children
          next_points += letter_node.points

      step(
        next_points,
        idx + 1,
        next_choices,
        next_stack,
      )

  step(root.points, 0, [], root.children)


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  s_high_str, *board_class = sys.argv[1:]
  cutoff = int(s_high_str)
  set_size(len(board_class))
  tree = build_orderly_tree(board_class, t)
  points = bound(tree)
  n_nodes = num_nodes(tree)
  sys.stderr.write(
    f"{board_class}: {points}, {n_nodes=}\n"
  )
  orderly_bound(tree, board_class, cutoff)


if __name__ == "__main__":
  main()


"""
Compare:

$ time poetry run python -m boggle.orderly_tree_builder 'lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz' --python --raw_multiboggle --bound 500 > /tmp/golden.txt
$ uv run src/listings/bound.py 500 lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz > /tmp/paper.txt

"""
