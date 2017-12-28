"""
了解slice
"""

class MySeq():
    def __getitem__(self, index):
        return index

s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])
print(s[1:4:2, 9])
print(s[1:4:2, 7:9])