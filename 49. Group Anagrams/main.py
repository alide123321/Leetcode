class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictHash = {}
        
        for i in range(len(strs)):
            dictHash.setdefault("".join(sorted(strs[i])), len(dictHash))

        output = [[] * len(dictHash) for i in range(len(dictHash))]
        
        for i in range(len(strs)):
            output[dictHash.get("".join(sorted(strs[i])))].append(strs[i])
    
        return output