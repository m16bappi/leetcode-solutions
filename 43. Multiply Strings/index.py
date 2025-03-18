"""
Multiply string between two numbers
"""

nums1 = "123"
nums2 = "456"
result = nums1

def multiplay(preNums, num):
    new_str = ""
    carry = 0
    for i in preNums[::-1]:
        multi = int(i) * int(num) + carry
        print(multi)
        if multi >= 10:
            carry = multi // 10
            rem = multi % 10
            new_str  = f"{rem}" + new_str
        else:
            new_str = f"{multi}" + new_str
    return new_str

for i in nums2[::-1]:
    result = multiplay(result, int(i))
    # print(result)

print(result)
