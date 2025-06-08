from listings.max_refactor import (
  set_size,
  max_bound,
)
from .util import get_enable2k_trie


def test_maxbound_fur_far():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(4)
  # far, arf
  assert 2 == max_bound(
    [
      "f",
      "au",
      ".",
      "r",
    ],
    t,
  )


def test_maxbound_big():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(9)
  assert 9460 == max_bound(
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
