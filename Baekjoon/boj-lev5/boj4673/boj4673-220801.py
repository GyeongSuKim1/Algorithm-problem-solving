nums = set(range(1, 10000))
remove_set = set()  
for i in nums :
    for j in str(i):
        i += int(j)
    remove_set.add(i)  

self_nums = nums - remove_set  
for i in sorted(self_nums):  
    print(i)