import functools
from listings.find_words import score
from trie import make_trie


@functools.lru_cache
def get_enable2k_trie():
  return make_trie("wordlists/enable2k.txt")


def test_find_words_small():
  t = get_enable2k_trie()
  assert 18 == score("abcdefghijklmnop", t)


def test_find_words_big():
  t = get_enable2k_trie()
  assert 3625 == score("perslatgsineters", t)
