nums=[]
while True:
    
    n=int(input())
    nums.append(n)
    print(nums)
    if len(nums)==3:
        m=input('you want the last number')
        if m=='no':
            del(nums[2])
            print(nums)
    
'''m=input('you want the last number')
if m=='no':
    del(nums[2])
    print(nums)'''
