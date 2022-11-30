pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
       mid = (l+u) //2
       if list[mid] == n:
          globals()['pos'] = mid
          return True
       else:
           if list[mid] < n:
              l = mid;
           else:
              u = mid;
list = [7,10,12,14,16,20,29,37]
n = 14
if search(list,n):
   print("Found at ",pos+1)
else:
   print("Not Found")

n = 29
if search(list,n):
   print("Found at ",pos+1)
else:
   print("Not Found")