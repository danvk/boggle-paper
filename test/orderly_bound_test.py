from listings.orderly_bound import (
  get_candidates,
  orderly_bound,
  set_size,
)
from listings.orderly import (
  build_orderly_tree,
)
from sum_choice_tree import bound
from .util import get_enable2k_trie


def test_orderly_bound():
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

  orderly_bound(tree, board_class, 700)
  candidate_boards = get_candidates()
  # None of these boards actually score 700+ points,
  # but their multiboggle score is high enough.
  assert set(candidate_boards) == {
    (722, "stseaetrd"),
    (741, "stseaetrg"),
    (759, "rtreaetsd"),
    (735, "rtseaetsd"),
    (711, "streaetsd"),
    (716, "rtsaeecrd"),
    (739, "stsaeecrd"),
    (804, "stsaeeprd"),
    (756, "stsaeeprg"),
    (775, "stsaeetrd"),
    (755, "stsaeetrg"),
    (775, "stseeecrd"),
    (704, "stseeecrg"),
  }
