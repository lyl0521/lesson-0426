# all()
print(all([0,1,2,3]))   #   False
print(all([1,2,3]))     #   True
print(all(['a','b','c','']))       # False
print(all(['a','b','c','d']))       #True

print(all(('a','b','c','d')))   #True
print(all(('a','b','','c')))    #False
print(all((0,1,2,3)))            #False
print(all((1,2,3)))              #True

print(all([]))  # True   empty list
print(all(()))  # True   empty tuple

# any()
# 如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
print(any(['a', 'b', 'c', 'd']))   #True
print(any(['a', 'b', '', 'd']))   #True
print(any([0, '', False]))         #False
print(any(('a', 'b', 'c', 'd')))   #True
print(any(('a', 'b', '', 'd')))   #True
print(any((0, '', False)))      #False
print(any([]))   #True
print(any(()))   #True

# bin()
# 返回整数的二进制表示
print(bin(int(10)))
print(bin(10))

