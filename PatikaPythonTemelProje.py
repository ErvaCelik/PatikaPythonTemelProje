#!/usr/bin/env python
# coding: utf-8

# # Ornek 1

# In[19]:



ornekListe1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
duzenlenmisListe = []

def flattenListe(liste):
    
    for eleman in liste:
        if type(eleman)== list:
            flattenListe(eleman)
        else:
            duzenlenmisListe.append(eleman)
    return duzenlenmisListe

flattenListe(ornekListe1)


# # Ornek 2

# In[20]:



ornekListe2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverseListe(liste):
    
    for eleman in liste:
        if type(eleman) == list:
            reverseListe(eleman)
    liste.reverse()
    return liste

reverseListe(ornekListe2)

