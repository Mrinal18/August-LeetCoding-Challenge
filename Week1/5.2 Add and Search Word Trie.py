#Using Trie

"""
In trie, each path from the root to the "word" node represents one of the input words, for example, o -> a -> t -> h is "oath".

Trie implementation is pretty straightforward, it's basically nested hashmaps. At each step, one has to verify, if the child node to add is already present. If yes, just go one step down. If not, add it into the trie and then go one step down.
"""

"""
Complexity Analysis

Time complexity: O(M) for the "well-defined" words without dots, where MM is the key length, and N is a number of keys, and O(M⋅N) for the "undefined" words. That corresponds to the worst-case situation of searching an undefined word (M + 1) times which is one character longer than all inserted keys.

Space complexity: O(1) for the search of "well-defined" words without dots, and up to \mathcal{O}(M)O(M) for the "undefined" words, to keep the recursion stack.
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.Trie
        
        for ch in word:
            
            if not ch in node:
                node[ch] = {}
                
            node = node[ch]
            
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    #if current char is '.'
                    #check for all the possibilities

                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i+1:], node[x]):
                                return True
                    #if no node lead to answer
                    #or if the current char is != '.'
                    return False
                    
                else:
                    node = node[ch]
            return '$' in node
        
        return search_in_node(word, self.Trie)
                                
                                
                            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
