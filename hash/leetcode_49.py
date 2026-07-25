class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)#创建一个字典，当访问一个不存在的 key 时，自动给这个 key 创建一个空列表 []。
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
#list(ans.values()) 是把 ans.values() 中的每一个值取出来并转换成一个普通列表，因此得到的是类似 [["eat","tea"], ["tan","nat"]] 的结果；而 [ans.values()] 只是新建了一个列表，
# 并把整个 ans.values() 对象作为这个列表的唯一元素，所以会变成 [dict_values(...)]。简单来说，list(x) 是“把 x 里面的元素变成列表”，而 [x] 是“把 x 整体装进列表”。