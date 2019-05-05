import os
import platform

print(os.name)

# print(os.uname())   # not for windows
print(platform.uname())

print(os.environ)
print(os.environ.get('PATH'))