from listings.orderly import (
  set_size,
  build_orderly_tree,
)
from sum_choice_tree import bound
from .util import get_enable2k_trie


def test_build_orderly_tree():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(4)
  tree = build_orderly_tree(
    ["ab", "cd", "ef", "gh"], t
  )
  assert bound(tree) == 8


def test_orderyl_tar_tier():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(4)
  tree = build_orderly_tree(
    ["t", "ae", "i", "r"], t
  )
  assert bound(tree) == 7
