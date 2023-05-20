#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Este código está sendo executado no jupyter!!!!!!!')


# In[2]:


inteiro = 10
decimal = 1.3
booleano = True
nulo = None

print(f'inteiro: {inteiro}, decimal: {decimal}, booleano: {booleano}, nulo: {nulo}')


# In[3]:


inteiro = 10
decimal = 1.3
booleano = True
nulo = None

print('inteiro: {}, decimal: {}, booleano: {}, nulo: {}'.format(inteiro, decimal, booleano, nulo))


# In[4]:


inteiro = int ('10') + 1
string = str(10)
print(inteiro, string)


# In[5]:


name = input('Enter your name: ')
print('Are you really', name, '?')


# In[7]:


string = 'abc'
print(string[0])
string[0] = 'b'


# In[8]:


a_list = []
L = [2, 'a', 4, [1,2]]
print(len(L)) #avalia para 4
print(L[0])   #avalia para 2
print(L[2]+1) #avalia para 5
print(L[3])   #avalia para [1,2], outra lista!
i=2 #
print(L[i-1]) #avalia para 'a' já que L[1] = 'a' acima


# In[9]:


a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
a.append(7)
print(a)


# In[10]:


nums = list(range(5))

print(nums)

print(nums[:]) # do início ao fim

print(nums[2:]) # do 2o (incluso) até o fim

print(nums[:2]) # do início ao 2o (excluso)

print(nums[2:4]) # do 2o (incluso) ao 4o (excluso)

print(nums[:-1]) # do início ao último (excluso)

nums[2:4] = [8, 9] # atribuição

print(nums)


# In[12]:


mixed = [1, 2, 'a', 3, 4.0]

mixed = [x**2 for x in mixed if type(x) == int]

print(mixed)


# In[13]:


lista = ['b', 'n', 'n']

lista1 = list(map(lambda x: x + 'a', lista))

print(lista1)


# In[14]:


l = [3, 'a', 4, 'b', 1, 4, 3]
l.sort()
print(l)


# In[15]:


x = [1, 2, 3]
y = [4, 5, 6]

for i, j in zip(x, y):
    print(i, j)


# In[16]:


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
tuples = list(enumerate(seasons))

print(tuples)


# In[17]:


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, season in enumerate(seasons):
    print(i, season)


# In[18]:


a = {1, 2, 3}
b = set([3, 4, 5])


# In[19]:


len(a)


# In[21]:


1 in a


# In[22]:


a ^ b


# In[23]:


a | b


# In[24]:


a - b


# In[25]:


a = {1, 2, 3}
b = set([3, 4, 5])


# In[28]:


c = {1, 2}


# In[30]:


a.issuperset(c)


# In[38]:


b.intersection(a)


# In[39]:


a = {1, 2, 3}
b = set([3, 4, 5])
c = {1, 2}


# In[40]:


c.issubset(a)


# In[41]:


d = {'camila': 21, 'roberto': 53, 'carla': 66}


# In[43]:


d['camila']


# In[44]:


# print d[21]  #resultará em um erro


# In[45]:


'camila' in d


# In[46]:


for key, value in d.items():
    print('chave', key, '\tvalor:', value)


# In[47]:


def func(a, norm=False):
    if norm: 
        return [(x - min(a))/ (max(a) - min(a)) for x in a]
    else: 
        return a
    
a = [1, 2, 3]
print(func(a))
print(func(a, False))
print(func(a, True))
print(func(a, norm=True))


# In[48]:


def func(*args):
    print(args)
    for item in args:
        print(item)
func(1, 2, 3, 'a', ['b, c'], 6.3)


# In[49]:


def func(a, b, c):
    print(f'a: {a}, b: {b}, c: {c}')
    
minha_lista = ['hello', 3, 1.7]
func(*minha_lista)


# In[50]:


def func(*args, **kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)
# func(10) error
func(10, param1=10, param2='hello', x=6.3)


# In[51]:


def func(a, b, c): 
    print('a: {}, b: {}, c: {}'.format(a, b, c))

params = {'a': 10, 'b': 'hello', 'c': 1.7}
func(**params) # é equivalente a func(a=params['a'], b=params['b'], c=params['c'])


# In[52]:


def func(a, b, c): 
    return a**2, b**3, c**4

a, b, c = func(2, 3, 4)
print(a, b, c)


# In[55]:


a = [1, 2, 4]
b, c, d = a
print(b, c, d)


# In[56]:


def my_func(some_list: list):
    for p in some_list:
        print(p)

a = [1, 2, 3]
my_func(a)


# In[57]:


def my_func(some_list: list) -> list:
    for i in range(len(some_list)):
        some_list[i] **= 2 #eleva cada membro da lista ao quadrado
    return some_list

a = [1, 2, 3]
my_func(a)


# In[58]:


def addOne(n):
    return n+1

def applyToEach(maxN, f):
    for i in range(1, maxN):
        print(f(i))
        
applyToEach(10, addOne)


# In[59]:


def f(x):
    return x**2
func = f
func(3.5)


# In[ ]:




