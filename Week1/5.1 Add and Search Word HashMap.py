#Using HashMap
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hash = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        self.hash[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        m = len(word)
        
        for dict_word in self.hash[m]:
            i = 0
            
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
            
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


"""
This solution passes all leetcode test cases, and formally has O(M.N) time complexity for the search, where MM is a length of the word to find, and NN is the number of words. Although this solution is not efficient for the most important practical use cases:

Finding all keys with a common prefix.

Enumerating a dataset of strings in lexicographical order.

Scaling for the large datasets. Once the hash table increases in size, there are a lot of hash collisions and the search time complexity could degrade to O(N^2 * M), where NN is the number of the inserted keys.
Trie could use less space compared to hashmap when storing many keys with the same prefix. In this case, using trie has only O(M⋅N) time complexity, where MM is the key length, and NN is the number of keys.
"""
