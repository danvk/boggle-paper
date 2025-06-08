from typing import Self, Sequence


class Trie:
    _children: dict[str, Self]
    _mark: int
    _is_word: bool
    _length: int
    _word: str

    def __init__(self):
        self._is_word = False
        self._mark = False
        self._children = {}

    def has_child(self, letter: str):
        return self._children.get(letter) is not None

    def child(self, letter: str):
        return self._children.get(letter)

    def is_word(self):
        return self._is_word

    def is_visited(self):
        return self._mark

    def set_visited(self):
        self._mark = True

    def length(self):
        return self._length

    def word(self) -> str:
        return self._word

    # ---

    def children(self) -> Sequence[Self]:
        return self._children.values()

    def set_is_word(self):
        self._is_word = True

    def add_word(self, word: str) -> Self:
        if word == "":
            self.set_is_word()
            return self
        letter = word[0]
        if not self.has_child(letter):
            self._children[letter] = Trie()
        return self.child(letter).add_word(word[1:])

    def size(self):
        return (1 if self.is_word() else 0) + sum(c.size() for c in self.children() if c)

    def num_nodes(self):
        return 1 + sum(c.num_nodes() for c in self.children() if c)

    def reset_marks(self):
        self._mark = False
        for child in self.children():
            if not child:
                continue
            child.reset_marks()


def is_boggle_word(word: str):
    size = len(word)
    if size < 3:
        return False
    for i, let in enumerate(word):
        if let < "a" or let > "z":
            return False
        if let == "q" and (i + 1 >= size or word[i + 1] != "u"):
            return False
    return True


def bogglify_word(word: str) -> str | None:
    if not is_boggle_word(word):
        return None
    return word.replace("qu", "q")


def make_trie(dict_input: str):
    t = Trie()

    for word in open(dict_input):
        word = word.strip()
        word = bogglify_word(word)
        if word is not None:
            n = t.add_word(word)
            n._length = len(word) + word.count("q")
            n._word = word
    return t
