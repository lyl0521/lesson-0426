# 定义类，实现字符串倒序输出

class Solution:

    def reverse_word(self,string):
        list = []
        for i in reversed(string):
            list.append(i)
        str = ''.join(list)
        return str

reverse = Solution()
print(Solution().reverse_word('Hello.py'))