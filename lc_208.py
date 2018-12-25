
class PrefixNode (object):
    def __init__(self):
        self.val = -1  # 0: not necessarily ends with node, 1: ends with node
        self.next = [None] * 26

class PrefixTree(object):
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word):
        n = self.root
        for idx in range(len(word)):
            w = word[idx]
            tmp = n.next[ord(w) - ord('a')]
            if not tmp:
                tmp = PrefixNode()
                n.next[ord(w) - ord('a')] = tmp

            tmp.val = 1 if idx == len(word) - 1 else max(tmp.val, 0)
            n = tmp

    def search(self, word):
        n = self.root
        if len(word) == 0: return True
        for idx in range(len(word)):
            w = word[idx]
            tmp = n.next[ord(w) - ord('a')]
            if not tmp:
                return -1
            else:
                if idx == len(word) - 1:
                    return tmp.val
                n = tmp
        return -1


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pTree = PrefixTree()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.pTree.insert(word)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ans = self.pTree.search(word)
        return ans == 1

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ans = self.pTree.search(prefix)
        return ans in [0, 1]
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)