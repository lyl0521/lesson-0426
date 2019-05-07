# 定义一个类，实现power

class Solution:

    def power(self, x, n):
        result = 1
        if n > 0:
            for i in range(1,n+1):
                result *= x
            return result
        if n < 0:
            for i in range(abs(n)):
                result /= x
            return result
        if n == 0:
            return 1

result = Solution().power(5,5)
print(result)
result = Solution().power(2,-3)
print(result)
result = Solution().power(100,0)
print(result)