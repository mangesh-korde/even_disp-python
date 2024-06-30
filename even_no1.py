#  Q..Write a python program take  n Numbers from user and store
#  it in list.. and display only even nos


n=input("Enter limit:")
n=int(n)
a=[]
for i in range(0,n):
     num=int(input("ENter No:"))
     a.append(num)
print(a)
print("Even nos:")
for i in range(0,n):
    if a[i]%2==0:
        print(a[i])
