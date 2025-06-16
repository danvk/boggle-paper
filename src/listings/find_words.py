import sys

from src.constants import SCORES, ALL_NEIGHBORS
from src.trie import Trie, make_trie

m = 4
n = 4
NEIGHBORS = ALL_NEIGHBORS[(m, n)]
lookup = None


# Listing 0: Scoring a Boggle Board
def score(bd: str, trie: Trie) -> int:
  used = {}

  def step(idx: int, node: Trie) -> int:
    score = 0
    used[idx] = True
    if node.has_child(bd[idx]):
      n = node.child(bd[idx])
      if n.is_word() and not n.is_visited():
        score += SCORES[n.length()]
        n.set_visited()
      for n_idx in NEIGHBORS[idx]:
        if not used.get(n_idx):
          score += step(n_idx, n)
    used[idx] = False
    return score

  return sum(
    step(i, trie) for i in range(m * n)
  )


# /Listing


def main():
  t = make_trie("wordlists/enable2k.txt")
  assert score("abcdefghijklmnop", t) == 18
  t.reset_marks()
  (board,) = sys.argv[1:]
  points = score(board, t)
  print(f"{board}: {points}")


if __name__ == "__main__":
  main()
