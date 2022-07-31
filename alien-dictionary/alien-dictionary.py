class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {}
        in_deg =  {}
        for word in words:
            for c in word:
                adj[c] = []
                in_deg[c] = 0
            
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    adj[c].append(d)
                    in_deg[d]+= 1
                    break
            else: 
                if len(second_word) < len(first_word): 
                    return ''
        
        res = []
        q = deque([ x for x, count in in_deg.items() if count == 0])
        visited = 0
        while q:
            v = q.popleft()
            res.append(v)
            visited += 1
            for nei in  adj[v]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
        return ''.join(res) if visited == len(in_deg) else ''
        
        
                
        