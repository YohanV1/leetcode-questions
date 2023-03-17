class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(len(set(zip(s,t))))
        return len(set(s))==len(set(zip(s,t)))==len(set(t))