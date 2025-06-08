from .util import get_enable2k_trie

from listings.find_words import score


def test_find_words_small():
  t = get_enable2k_trie()
  t.reset_marks()
  assert 18 == score("abcdefghijklmnop", t)


def test_find_words_big():
  t = get_enable2k_trie()
  t.reset_marks()
  assert 3625 == score("perslatgsineters", t)
