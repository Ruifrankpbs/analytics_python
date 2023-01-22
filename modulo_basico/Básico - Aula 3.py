#!/usr/bin/env python
# coding: utf-8

# #  Funções Definidas pelo Usuário, Loops e Operadores Condicionais

# ## Parte 1 - Funções Definidas pelo Usuário

# In[ ]:





# ## Como Definir uma função

# ### O objetivo das funções é simplificar operações recorrentes para poderem ser chamadas apenas passando o nome da função e o argumento
# 
# ### Sintaxe:
# 
# #### def funcao (argumentos) ou lambda x:
# 
# ### Observação:
# #### É importante prever se  é necessário definir um valor padrão para os argumentos.

# In[ ]:





# In[2]:


import pandas as pd
import numpy as np


# In[3]:


base = pd.read_csv(r'/Users/ruifrankpintooliveira/Documents/Codigo+e+Datasets+-+Atualizado+20220807 (1)/Aula 2/train.csv')


# In[4]:


base


# In[11]:


texto = 'Brenda Camila'


# In[13]:


texto[0] + texto[-1] + ' - Final'


# In[18]:


def funcaobrenda(texto):
    return(texto[0]+text[-1]+' - Final')


# In[66]:


funcaobrenda('Rui Frank')

