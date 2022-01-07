#!/usr/bin/env python
# coding: utf-8

# # Loops

# There are 2 types of Python loops - for and while.

# In[ ]:


Soprano_family_Capos = ["Sil","T","Paulie","Gino"]
NY_capos = ["Coco","Butch","Phil","Carmine"]

Sopranos_show_capos = Soprano_family_Capos + NY_capos
print(Sopranos_show_capos)


# In[ ]:


for NY_capos in Sopranos_show_capos:
    print(Soprano_family_Capos)


# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, which acts like xrange).

# In[ ]:


# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
#Note that when you add a 3rd number in range(), this is how many numbers to count. For example, 3 would mean counting every third number.#


# ## "While" loops

# While loops repeat as long as a certain boolean condition is met - 

# In[ ]:


count = 0
while count < 6:
    print(count)
    count += 2


# ## "Break" and "Continue" Statements

# Break is used to a exit a loop. Continue is used to skip the current block and return to the "for" and "while" statement. 

# In[ ]:


count = 1
while True:
    print(count)
    count += 1
    if count >= 10: 
         break
        


# In[ ]:


#Prints out only odd numbers#
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


# The 'continue' part tells Python to skip over objects that don't satisfy the 'if' statement included.

# In[ ]:


a = 1
b = 2
while a < 5:
    b += a
    a += 1
    print(b)


# ## The 'else' clause in loops

# Unlike C, 'else' can be used in loops. When the loop condition of 'for' or 'while' 'fails' then the code in 'else' is executed. If a break statement is executed inside the for loops then 'else' is skipped.
# 
# 'Else' is executed even if there is a continute statement. 

# In[ ]:


count = 1
while(count<10):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


# In[ ]:


for i in range (1,20):
    if(i%5==0):
        break
    print(i)
else:
    print("The break statement was inside the for loop and so 'else' was skipped")


# In[ ]:


for i in range (1,10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("i value reached %d" % (i)) 


# In[ ]:


count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value rached %d" % (count))


# In[ ]:


names = ["John","Jane"]
foods = ["pizza","sushi","burgers"]
for name in names:
    for food in foods:
        print(name + "likes" + food)


# In[ ]:


a = ['foo','bar','baz']
while True:
    if not a:
        break
    print(a.pop())


# In[ ]:


a = ['foo','bar','baz']
while a:
    print(a.pop())


# In[ ]:


for True:
    if not a:
        break
    print(a.pop())


# In[ ]:


do:
    if not a:
        break
    print(a.pop())
while True


# ## Exercise

# Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.

# In[ ]:


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for x in numbers:
    if x % 2 == 0:
        print(x)
    if x == 237: 
         break


# In[ ]:


x = 0
while x < 5:
    print(x)
    x += 1


# In[8]:


#Prints out only even numbers within the range
for x in range(10):
    if x % 2 != 0:
        continue
    print(x)


# In[9]:


#Prints out exactly 10 iterations
for n in range(10,20,1):
    print(n)


# In[10]:


a = 2
b = 3
while a < 10 :
    b += a
    a += 2
print(b)


# In[ ]:


primes = [2,3,5,7]
for prime in primes:
    print(primes)


# In[ ]:


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        endwhile


# ## Iterating over a range of numbers

# In[2]:


for x in range(5):
    print(x)


# In[3]:


numbers = range(5)
for i = 1; i < len(numbers); i += 1:
    print(numbers[i])


# In[4]:


x = 0
repeat:
    print(x)
    x += 1
until x > 5

