from listings.add_word import (
  set_size,
  build_tree_alt,
)
from sum_choice_tree import bound
from .util import get_enable2k_trie


def test_maxtree_big():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(9)
  assert 9460 == bound(
    build_tree_alt(
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
