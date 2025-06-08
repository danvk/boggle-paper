from listings.max_tree import (
  set_size,
  build_tree,
)
from sum_choice_tree import bound
from .util import get_enable2k_trie


def test_maxtree_fur_far():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(4)
  # far, arf
  assert 2 == bound(
    build_tree(
      [
        "f",
        "au",
        ".",
        "r",
      ],
      t,
    )
  )


def test_maxtree_big():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(9)
  assert 9460 == bound(
    build_tree(
      [
        "lnrsy",
        "chkmpt",
        "lnrsy",
        "aeiou",
        "aeiou",
        "aeiou",
        "chkmpt",
        "lnrsy",
        "bdfgjqvwxz",
      ],
      t,
    )
  )
