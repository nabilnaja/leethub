class Codec:
    max_size = 3
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for word in strs:
            encoded.extend([f"{len(word):03d}", word])
        return ''.join(encoded)
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
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