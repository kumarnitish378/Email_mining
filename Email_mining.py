#!/usr/bin/env python
# coding: utf-8

# In[67]:


with open("PEmails.txt",'r',encoding="utf8") as f:
    data = f.read()
    a = data.split()
    email = []
    for i in a:
        if "@" in i and len(i)>5:
            if "id--" in i:
                i=i.replace('id--',"")
            if "Email-" in i:
                i=i.replace('Email-',"")
            if 'e-mail -' in i:
                i=i.replace('e-mail -',"")
            if 'id-' in i:
                i=i.replace('id-',"")
            if '-' in i:
                i=i.replace('-',"")
            if "EMAIL=" in i:
                i = i.replace('EMAIL=','')
            if " " in i:
                i = i.replace(' ','')
            email.append(i)
#             print(i, file=open("email.txt",'a'))
#     print(email)


# In[ ]:





# In[ ]:





# In[ ]:




