### higher order function - map(function,iterable)##
number = [5,4,6,8]
def square(x):
    return x * x
squared = list(map(square,number))
print(squared)

## filter(function,iterable) ##
n = [3,6,2,5,9]
def is_even(x):
    return x %2 == 0
evens = list(filter(is_even,n))
print(evens)

## reduce(function,iterable) ##
n = [2,3,4]
def multiply(x,y):
    return x*y
result = n[0]
for num in n[1:]:
    result = multiply(result,num)
print("Product of all numbers : ",result)

### sorted(iterable,key=function) ##
names = ["Sham","Shivani","Aradhana","Ram"]
sorted_names = sorted(names,key=len)  
print(sorted_names)

## any(iterable) ##
values = [1,False,3]
print(any(values))

## all(iterable) ##
values = [4,True,3,"ARa"]
print(all(values))