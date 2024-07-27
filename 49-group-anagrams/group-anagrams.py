class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            if ''.join(sorted(word)) in hashmap:
                hashmap[''.join(sorted(word))].append(word)
            else:
                hashmap.update({''.join(sorted(word)): [word]})

        res = []
        for w, val in hashmap.items():
            print(val)
            res.append(val)

        return res
        