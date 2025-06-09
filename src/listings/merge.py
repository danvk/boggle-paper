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
from util import find

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
  orderly_set_size(num_cells)


ORDER = SPLIT_ORDER[(4, 4)]


# Listing 9: merge operation on orderly trees
# merge: (Orderly(N), Orderly(N)) -> Orderly(N)
def merge(a: SumNode, b: SumNode) -> SumNode:
  by_cell = {c.cell: c for c in a.children}
  for bc in b.children:
    ac = by_cell.get(bc.cell)
    by_cell[bc.cell] = (
      merge_choice(ac, bc) if ac else bc
    )
  ch = sorted(
    by_cell.values(),
    key=lambda c: -ORDER[c.cell],
  )
  return SumNode(
    points=a.points + b.points, children=ch
  )


# merge_choice: (OrderlyChoice(N), OrderlyChoice(N))
#               -> OrderlyChoice(N)
def merge_choice(
  a: ChoiceNode, b: ChoiceNode
) -> ChoiceNode:
  ch = {**a.children}
  for choice, bc in b.children.items():
    ac = ch.get(choice)
    ch[choice] = merge(ac, bc) if ac else bc
  return ChoiceNode(cell=a.cell, children=ch)


# /Listing


# Listing 10: branch operation on orderly trees
# branch: Orderly(N) -> list(Orderly(N-1))
def branch(
  o: SumNode,
  N: int,
  board_class: list[str],
) -> list[SumNode]:
  top_choice = find(
    o.children, lambda c: c.cell == N
  )
  if not top_choice:
    # cell is irrelevant; o is Orderly(N-1)
    return [o for _ in board_class[N]]

  other_choices = [
    c for c in o.children if c.cell != N
  ]
  skip_tree = SumNode(
    children=other_choices, points=o.points
  )  # Orderly(N-1)
  return [
    merge(
      top_choice.children[letter], skip_tree
    )  # both are Orderly(N-1)
    if top_choice.children.get(letter)
    else skip_tree  # dead letter on cell N.
    for letter in board_class[N]
  ]


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

  split_order = SPLIT_ORDER[(m, n)]
  cell = split_order[0]
  subtrees = branch(tree, cell, board_class)
  assert len(subtrees) == len(
    board_class[cell]
  )
  for letter, subtree in zip(
    board_class[cell], subtrees
  ):
    b = bound(subtree)
    nn = num_nodes(subtree)
    print(
      f"  {cell=} {letter=} bound={b} num_nodes={nn}"
    )


if __name__ == "__main__":
  main()

"""
Compare:

$ time poetry run python -m boggle.orderly_tree_builder 'lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz' --force --python --raw_multiboggle
1.56s OrderlyTreeBuilder: t.bound=1523, 333492 nodes
  cell=4 letter='a' t.bound=1198, 86420 nodes
  cell=4 letter='e' t.bound=1417, 98585 nodes
  cell=4 letter='i' t.bound=994, 81062 nodes
  cell=4 letter='o' t.bound=862, 75474 nodes
  cell=4 letter='u' t.bound=753, 60457 nodes
poetry run python -m boggle.orderly_tree_builder  --force --python   2.77s user 0.08s system 95% cpu 2.984 total

$ uv run src/listings/merge.py lnrsy chkmpt lnrsy aeiou aeiou aeiou chkmpt lnrsy bdfgjqvwxz
['lnrsy', 'chkmpt', 'lnrsy', 'aeiou', 'aeiou', 'aeiou', 'chkmpt', 'lnrsy', 'bdfgjqvwxz']: 1523, n_nodes=333492
  cell=4 letter='a' bound=1198 num_nodes=86420
  cell=4 letter='e' bound=1417 num_nodes=98585
  cell=4 letter='i' bound=994 num_nodes=81062
  cell=4 letter='o' bound=862 num_nodes=75474
  cell=4 letter='u' bound=753 num_nodes=60457
poetry run python -m paper.78_merge_branch lnrsy chkmpt lnrsy aeiou aeiou      3.59s user 0.08s system 96% cpu 3.806 total

"""
