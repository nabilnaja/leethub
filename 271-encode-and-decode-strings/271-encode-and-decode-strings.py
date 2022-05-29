class Codec:
    max_size = 3
    def encode(self, strs: List[str]) -> str:
        """
        Time complexity: O(n * k).  n is the numberof strings and k the length of the longuest one
        Space complexity:  O(n * k)
        """
        encoded = []
        for word in strs:
            encoded.extend([f"{len(word):03d}", word])
        return ''.join(encoded)
            
        

    def decode(self, s: str) -> List[str]:
        """
        Time complexity: O(n)
        Space complexity:  O(n)
        """
        if not s: 
            return []
        decoded = []
        i = 0
        while i < len(s):
            word_index = i + Codec.max_size
            word_size = int(s[i:word_index])
            word_end = word_size + word_index
            decoded.append(s[word_index: word_end])
            i = word_end
        return decoded 
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))