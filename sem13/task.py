st =input()
nums=st.split()
for i in range (len(nums)):
    nums[i]=int(nums[i])


def is_positive(num) -> bool:
    if num >= 0:
        return True
    else:
        return False


def count_positive(number:list) -> int:
    count = 0
    for j in number:
        if is_positive(j):
            count += 1
    return count

def count_negative(number:list) -> int:
    count = 0
    for f in number:
        if is_positive(f):
            count += 0
        else:
            count += 1
    return count

print(count_positive(nums))
print(count_negative(nums))