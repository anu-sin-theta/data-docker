import numpy as np
print(np.__version__)
array = np.array([[1,2,3,4,5],[6,7,8,9,0]],dtype="int64")
print(array.size)
print(array.shape)
if array.ndim == 1:
    print("1D array")
else:
    pass
    #to check elements of array are zero or not
print(np.all(array)) #if all elements are zero then it will return false
    #to check elements of array are non zero or not
print(np.any(array)) #if any element is non zero then it will return true
    #to check elements of array are even or not
print(np.all(array%2==0)) #if all elements are even then it will return true
print(np.sin(90))
print(np.exp(1))#e^1
print(np.log(2))#log2
print(np.log10(2))#means log10 base 2
print(np.iscomplex(1+2j))
print(np.isreal(1+2j))
print(np.isreal(1))
print(np.reshape(array,(5,2)))
e = np.random.choice([1,2,3,4,5,6,7,8,9], (3,4))
print(e)
print(np.sort(e))#sorts the array in ascending order
print(np.argsort(e))#sorts the array in ascending order and returns the index of the elements
print(np.argmax(e))#returns the index of the maximum element, 9 ka index 6 hai
print(np.argmin(e))
print(np.max(e))#returns the maximum element
print(np.diag(e))#e ka matlab hai ki e ki diagonal elements print karo, agar e 2d array hai toh diagonal elements print karo
a= np.array([1,2,3,4,5])
g= np.random.rand(3,4)
print(a)
b = np.random.randint(1,10,6)#Create a 1d array of size 6 with random integers between 1 to 10
print(b)
c = np.random.randint(1,10,(3,4)) #this is a 3x4 matrix
print(c)
d= np.ones((c.shape))
print(d)
print(np.shares_memory(c,d))
e= np.random.choice([1,2,3,4,5,6,7,8,9], (3,4))
print(e)
f= np.round(np.random.random((3,4)),2)
print(f.shape)
s= np.reshape(f,(2,6))
print(s)
n= s.reshape(-1)#-1 ka matlab hai ki jitne bhi rows ho utne hi columns ho aur vice versa
print(n)




