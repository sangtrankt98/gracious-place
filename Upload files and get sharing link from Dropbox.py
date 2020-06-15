#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# => FullAccount(account_id='dbid:AAAarvRGkrPqpjU2NU8AmOD8SF93jsv_0UA',
# the source file
import pathlib
import re
import dropbox as dx
import glob
import pandas as pd
dir_to_scan='C:/Users/ftt.sang.tran/Downloads/Tables Grab/New Folder'
folder=pathlib.Path(dir_to_scan)
def sang():
    result=[]
    for i in folder.glob('*.*'):
        target = "/VN_Mex/"            
        targetfile = target + i.name
        d = dx.Dropbox('LUZ0DHgfXvAAAAAAAAAIbONov4OfXjy_W3XOlKfiFmQ7vsohMjK3qIBBf1xh6rcJ')
        with i.open("rb") as f:
            meta = d.files_upload(f.read(), targetfile, mode=dx.files.WriteMode("overwrite"))
            link = d.sharing_create_shared_link(targetfile)
            url = link.url
        result.append(url)
    return result
sang()
dict0={'Link':sang()}
df=pd.DataFrame(dict0)
df.to_excel('C:/Users/ftt.sang.tran/Downloads/Tables Grab/Result.xlsx',index = False)


# In[ ]:




