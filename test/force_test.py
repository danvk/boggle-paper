from listings.force import (
  set_size,
  forced_tree,
)
from .util import get_enable2k_trie


def test_force():
  t = get_enable2k_trie()
  t.reset_marks()
  set_size(4)
  bc = ["ab", "cd", "ef", "gh"]
  assert forced_tree(bc, "aceh", t) == 4
  t.reset_marks()
  assert forced_tree(bc, "beef", t) == 6

  t.reset_marks()
  set_size(6)
  assert forced_tree(["x"], "efeebe", t) == 12
