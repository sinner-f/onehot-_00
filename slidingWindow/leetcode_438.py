class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        for right,item in enumerate(s):
            cnt_s[item] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            cnt_s[s[left]] -= 1
        return ans