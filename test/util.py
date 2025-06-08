import functools
from trie import make_trie


@functools.lru_cache
def get_enable2k_trie():
  return make_trie("wordlists/enable2k.txt")
