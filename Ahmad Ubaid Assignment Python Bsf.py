#!/usr/bin/env python
# coding: utf-8

# In[16]:


graph={ "s":["A","B"],
        "A":["C","D"],
        "B":["E","F"],
        "C":["G","H"],
        "D":["M","N"],
        "E":["O","P"],
        "F":["W","X"],
        "G":[],
        "H":["I","J"],
        "M":[],
        "N":[],
        "O":[],
        "P":["Q","R"],
        "W":[],
        "X":["Y","Z"],
        "I":[],
        "J":["K","L"],
        "Q":[],
        "R":["S","T"],
        "Y":[],
        "Z":["*","+"],
        "K":[],
        "L":[],
        "S":["U","V"],
        "T":[],
        "*":[],
        "+":[],
        "U":[],
        "V":[]   
      }


# In[17]:


start="s"
visit = [start]
queue = [start]
BSF_Output = []
Goal="+"


# In[18]:


while len(queue)!=0:
    
    if queue[0]==Goal:
        v = queue[0]
        BSF_Output.append(v)
        print("BSF Output:",BSF_Output)
        break  
        
    else:
        
        v = queue[0]
        BSF_Output.append(v)
        queue = queue[1:]
        

        for n in graph[v]:
            if n not in visit:
                visit.append(n)
                queue.append(n)


# In[ ]:




