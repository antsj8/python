#!/usr/bin/env python
# coding: utf-8

# ### Automatic File Sorter

# In[1]:


import os, shutil


# In[43]:


path = r'C:\Users\antho\OneDrive\Documents\Automatic Sorter\\'


# In[44]:


os.listdir(path)


# In[45]:


#os.makedirs(path + new_folder_name)


# In[46]:


folder_names = ['CSV Files','Text File','Image Files']

#C:\Users\antho\OneDrive\New folder\Automatic_SorterImage Files'

for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
    


# In[ ]:





# In[47]:


os.listdir(path)


# In[55]:


file_names = os.listdir(path)
path = r'C:\Users\antho\OneDrive\Documents\Automatic Sorter\\'


# In[57]:


for file in file_names:
    if ".csv" in file and not os.path.exists(path + "CSV Files\\" + file):
        shutil.move(path + file, path + "CSV Files\\" + file)
    elif ".png" in file and not os.path.exists(path + "Image Files\\" + file):
        shutil.move(path + file, path + "Image Files\\" + file)
    elif ".txt" in file and not os.path.exists(path + "Text File\\" + file):
        shutil.move(path + file, path + "Text File\\" + file)


# In[58]:


path = r'C:\Users\antho\OneDrive\Documents\Automatic Sorter\\'

folder_names = ['CSV Files','Text File','Image Files']



for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
        
        
file_names = os.listdir(path)

for file in file_names:
    if ".csv" in file and not os.path.exists(path + "CSV Files\\" + file):
        shutil.move(path + file, path + "CSV Files\\" + file)
    elif ".png" in file and not os.path.exists(path + "Image Files\\" + file):
        shutil.move(path + file, path + "Image Files\\" + file)
    elif ".txt" in file and not os.path.exists(path + "Text File\\" + file):
        shutil.move(path + file, path + "Text File\\" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




