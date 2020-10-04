#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

import time
import chardet

#module
def is_unique_chars2(str_obj:str)->bool:
    """
    input:String(ASCII)
    output:Bool
    This module determine a unique string.
    """
    if chardet.detect(str_obj)['encoding'] != 'ascii':
        return False
    
    bool_list = [False]*256
    for i in str_obj:
        if bool_list[i] == True:
            return False
        bool_list[i] = True
    return True

#test
def is_unique_chars2_test():
    #False
    test1 = 'jis-26000'.encode('utf-8')
    test2 = 'あいうえおabc'.encode('utf-8')
    #True
    test3 = 'abcdef'.encode('utf-8')
    if is_unique_chars2(test1) == True:
        return exit()
    if is_unique_chars2(test2) == True:
        return exit()
    if is_unique_chars2(test3) == False:
        return exit()
    print("OK!")
    
is_unique_chars2_test()


# In[ ]:




