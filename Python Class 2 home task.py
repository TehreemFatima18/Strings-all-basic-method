#!/usr/bin/env python
# coding: utf-8

# # 20 operands with different operators

# In[135]:


154 + 40 / 8 + (((( 13 + 5 )* 2)- 4)/ 2)- 21 / 7 + 18 * 32 % 5 - 12 + 400 + 180 * 38 / 4 + 23 * 12
# 154 + 40 / 8 +  16 -21 / 7 + 18 * 32 % 5 - 12 + 400 + 180 * 38 / 4 + 23 * 12
# 154 + 5 + 16 - 3 + 576 % 5 -12 + 400 + 180 * 9.5 + 276.
# 154 + 5 + 16 - 3 + 1 - 12 + 400 + 1710 + 276
# 176 - 3 - 12 + 2386 
# 2562 - 15
# 2547


# #  All String data type Methods

# In[136]:


name = "Hello World!. This is my World."
dir(name)


# In[137]:


name.capitalize()


# In[138]:


name.casefold()


# In[139]:


x="Barbican"
x.center(40)


# In[140]:


name.count("l")


# In[141]:


name.count("World")


# In[142]:


name.encode()


# In[143]:


name.endswith("!")


# In[144]:


name.endswith(".")


# In[145]:


r="\tRest\t"
r.expandtabs(4)


# In[146]:


r="\tR\te\ts\tt\t"
r.expandtabs(25)


# In[147]:


name.find("l")


# In[148]:


txt = "My name is {fname}, I'am {age}".format(fname = "nick", age = 26)
print(txt)


# In[149]:


name.format()


# In[150]:


name.format_map("")


# In[151]:


# input stored in variable a. 
a = {'x':'John', 'y':'Wick'} 
  
# Use of format_map() function 
print("{x}'s last name is {y}".format_map(a)) 


# In[152]:


name.index("r")


# In[153]:


name.index("World")


# In[154]:


name.isalnum()


# In[155]:


txt="5afgdjk"
txt.isalnum()


# In[156]:


name.isalpha()


# In[29]:


a="World"
a.isalpha()


# In[30]:


name.isascii()


# In[31]:


a.isascii()


# In[32]:


txt.isascii()
#print(ascii(txt))
#'5afgdjk'
#print(ascii('°'))
#'\xb0'


# In[34]:


name.isdecimal()


# In[35]:


txt.isdecimal()


# In[36]:


b="3456"
b.isdecimal()


# In[37]:


name.isdigit()


# In[41]:


b.isdigit()


# In[42]:


name.isidentifier()


# In[43]:


c="hjkjlll"
c.isidentifier()


# In[44]:


name.islower()


# In[45]:


c.islower()


# In[46]:


name.isnumeric()


# In[47]:


x="35467898760"
x.isnumeric()


# In[48]:


name.isprintable()


# In[49]:


txt = "Hello!\nAre you #1?"
txt.isprintable()


# In[50]:


name.isspace()


# In[51]:


x.isspace()


# In[52]:


y="      "
y.isspace()


# In[53]:


name.istitle()


# In[54]:


title="This Is My World"
title.istitle()


# In[55]:


name.isupper()


# In[56]:


name.upper()


# In[57]:


name.isupper()


# In[58]:


z="HELLO, AND WELCOME TO MY WORLD"
z.isupper()


# In[114]:


list=['1','3','5','7','9']
a= " # "
a.join(list)


# In[65]:


myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


# In[100]:


txt="apple"
x=txt.ljust(50," ")
x


# In[115]:


list1 = ['a','p','p','l','e']
print("".join(list1))


# In[157]:


txt="apple"
x=txt.ljust(50,"0")
x


# In[103]:


txt="apple"
x=txt.ljust(20)
x


# In[106]:


name.lower()


# In[109]:


fruit= "     pineapple   "
fruit.lstrip()


# In[124]:


string = "This is a string example"
intab = "aeiou"
outtab = "12345"
tab = string.maketrans(intab, outtab)
print(tab)
print(string.translate(tab))


# In[122]:


name.partition("This") #makes a tuple by parting into three sectons


# In[168]:


sent="This is my World, World is beautiful"
print(sent.replace("World", "Land"))


# In[165]:


txt= "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


# In[166]:


str = "this is string example....wow!!! this is really string"
print(str.replace("is", "was"))
print(str.replace("is", "was", 3))


# In[171]:


name ="Hello World!. This is my World."
name.rfind("l")


# In[172]:


name.rindex("World")


# In[179]:


d= "pineapple is love"
d.rjust(40)


# In[181]:


name.rpartition("World")


# In[182]:


name.rsplit(",")


# In[184]:


fruit="apple, banana, guava, berry"
fruit.rsplit(",")


# In[186]:


r = "  it is here.        "
r.rstrip()


# In[187]:


name.split()


# In[188]:


name.splitlines()


# In[189]:


txt = "Thank you for the music\nWelcome to the jungle"
txt.splitlines()


# In[190]:


name.startswith("W")


# In[191]:


name.startswith("H")


# In[208]:


name= "      Hello World           " #remove spaces
name.strip()


# In[193]:


name.swapcase()


# In[196]:


txt="My name is tehreem fatima"
txt.title()


# In[205]:


# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))


# In[209]:


name.upper()


# In[202]:


name="Hello World"
name.zfill(20)


# In[ ]:




