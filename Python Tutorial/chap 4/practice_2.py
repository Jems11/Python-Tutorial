# accept makrs of 6 students & display them in sorted manner
m1 = int(input("enter the marks for student Number 1 : "))
m2 = int(input("enter the marks for student Number 2 : "))
m3 = int(input("enter the marks for student Number 3 : "))
m4 = int(input("enter the marks for student Number 4 : "))
m5 = int(input("enter the marks for student Number 5 : "))
m6 = int(input("enter the marks for student Number 6 : "))

mylist = [m1,m2,m3,m4,m5,m6]
mylist.sort()
print(mylist)