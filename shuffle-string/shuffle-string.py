class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        final = [0] * len(indices)
        
        for i, char in enumerate(s):
            index = indices[i]
            final[index] = char
        return ''.join(final)