with open('1.txt','r') as f:
    nums = [int(x) for x in f.readlines()]
print(sum(nums))
