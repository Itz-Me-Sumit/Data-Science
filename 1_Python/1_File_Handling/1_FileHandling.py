#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os


# In[ ]:


os.getcwd()


# In[ ]:


os.listdir(r'c:\\Users\\sumit\\OneDrive\\Desktop\\Data Science')


# In[ ]:


os.path.join( os.getcwd() , 'text.txt' , 'abc')


# In[ ]:


# open file

with open('test.txt' , 'r') as file:
    print(file.readlines())


# In[ ]:


full_path = os.path.join(os.getcwd() , 'test.txt')
print(full_path)

file2 = open(full_path , 'r')
print(file2.read())
file2.close()


# In[ ]:


with open('./test.txt' , 'w') as f:
    lines = ["heyyy.. so it is 2nd line\n" , "and this is my 3rd line\n"]
    f.write("so it's first line ayooo\n")
    f.writelines(lines)


# In[ ]:


with open('./test.txt' , 'a') as f:
    f.write("hell yeahh i'm appending my 6th line\n")


# In[ ]:


with open("./dummy.txt" , 'a+') as f:
    f.write("Hello it is first line\n")
    f.write("THis is second line\n")


# In[ ]:


with open("./dummy.txt" , 'a+') as f:
    f.write("and it is third line\n")
    f.write("THis is fourth line\n")


# In[ ]:


with open("./dummy.txt" , 'a+') as f:
    f.seek(0)
    content = f.read()
    print(content)


# In[ ]:




