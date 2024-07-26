class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_map, t_map = {}, {}

        for l in s:
            if l in s_map:
                s_map[l] += 1
            else:
                s_map.update({l:1})

        for l in t:
            if l in t_map:
                t_map[l] += 1
            else:
                t_map.update({l:1})
        

        for letter in s_map:
            print(letter)
            if s_map[letter] != t_map.get(letter, 0):
                return False
        
        return True


            
        
        