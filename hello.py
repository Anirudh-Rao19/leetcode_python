name="ani"
print(f"hello {name}")
a="hello"
for i in a:
    print(i)
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
j=0
for i in range(m,m+n):
    nums1[i]=nums2[j]
    j+=1
print(sorted(nums1))