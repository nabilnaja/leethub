class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = 'a'
        counter_size = 27
        hashmap = defaultdict(list)
        for word in strs:
            counter = [0 for _ in range(counter_size)]
            for char in word:
                counter[ord(char) - ord(a)] += 1
            hashmap[tuple(counter)].append(word)
        return hashmap.values()
                
            
                
        