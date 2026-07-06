class Trie:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        
        node = self
        
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            
            node = node.children[char]


    def search(self, word: str) -> bool:
        
        node = self

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return len(node.children) == 0

    def startsWith(self, prefix: str) -> bool:
        
        node = self
        
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    trie = Trie()

    operations = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    arguments = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected = [None, None, True, False, True, None, True]

    results = [trie]

    for operation, argument in zip(operations[1:], arguments[1:]):
        results.append(getattr(trie, operation)(*argument))

    print(results)
    print(expected)