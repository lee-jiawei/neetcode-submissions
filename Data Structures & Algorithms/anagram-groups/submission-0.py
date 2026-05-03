class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)): 
            if str(sorted(strs[i])) in dict: 
                dict[str(sorted(strs[i]))].append(strs[i])
            else:
                dict[str(sorted(strs[i]))] = [strs[i]]
        return list(dict.values())