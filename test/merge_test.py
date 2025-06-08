from listings.merge import branch
from listings.orderly import (
  set_size,
  build_orderly_tree,
)
from sum_choice_tree import bound
from .util import get_enable2k_trie


def test_build_orderly_tree():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(9)
  board_class = [
    "lnrsy",
    "chkmpt",
    "lnrsy",
    "aeiou",
    "aeiou",
    "aeiou",
    "chkmpt",
    "lnrsy",
    "bdfgjqvwxz",
  ]
  tree = build_orderly_tree(board_class, t)
  assert bound(tree) == 1523

  subtrees = branch(tree, 4, board_class)
  assert len(subtrees) == len(board_class[4])
  assert bound(subtrees[0]) == 1198
  assert bound(subtrees[1]) == 1417
  assert bound(subtrees[2]) == 994
  assert bound(subtrees[3]) == 862
  assert bound(subtrees[4]) == 753
