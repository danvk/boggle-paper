from listings.sumbound import set_size, sum_bound
from .util import get_enable2k_trie


def test_sumbound_big():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(9)
  assert 109524 == sum_bound(
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
