class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time complexity: O(n * k), n is the number of words, k is the length of the longuest word 
        Space complexity:  O(n * k), n and k are the same as for the TS. this space is occupied by the hashmap
        """
        a = 'a'
        counter_size = 27
        hashmap = defaultdict(list)
        for word in strs:
            counter = [0 for _ in range(counter_size)]
            for char in word:
                counter[ord(char) - ord(a)] += 1
            hashmap[tuple(counter)].append(word)
        return hashmap.values()
                
            
                
        