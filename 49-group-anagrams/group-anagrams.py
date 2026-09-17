class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        new_dict ={}
        for word in strs:
            key = tuple(sorted(word))
            if key not in new_dict:
                new_dict[key] = []
            new_dict[key].append(word)
        new_list =[]
        return list(new_dict.values())

