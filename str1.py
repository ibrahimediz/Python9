#!/usr/bin/env python
# coding: utf-8

# In[2]:


metin = "Yaşamak bir ağaç gibi tek ve hür ve bir orman gibi kardeşçesine"
metin[0:7:2]


# In[5]:


metin.split()


# In[6]:


metin.split("bir")


# In[12]:


metin = "----------------Beşiktaş-------------------"
metin


# In[21]:


metin.strip("-")


# In[22]:


metin.upper()


# In[30]:


metin.lower()


# In[33]:


metin = "yaşamak bir ağaç gibi tek ve hür ve bir orman gibi kardeşçesine"


# In[36]:


metin.replace(" ","-")


# In[38]:


metin.endswith("çe")


# In[1]:


adi = input("Adı")
soyadi = input("Soyadı")
davet = "sayın {1} {0},sizi ve ailenizi aramızda görmekten mutluluk duyarız".format(adi,soyadi)


# In[12]:


metin =  "1-2--"
davet.join(metin).split("-")


# In[41]:


metin.rfind("bir")


# In[13]:


metin = "yaşamak bir ağaç gibi tek ve hür ve bir orman gibi kardeşçesine"


# In[14]:


metin.replace(" ","-").replace("a","â")


# In[20]:


adi = "deneme' OR '1'='1"
sorgu = "SELECT * FROM TABLO where ADI = '{}'".format(adi)
sorgu.replace("OR","")


# aaaa

# In[ ]:





# In[ ]:




