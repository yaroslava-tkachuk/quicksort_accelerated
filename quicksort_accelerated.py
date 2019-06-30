
# coding: utf-8

# In[1]:


'''This module contains an accelerated versoin of quicksort (recursieve version).

Insertion sort is used for sets of data which are under certain length (parameter mod_len which is 10 by default and can be modified).
Quicksort worst-case performance: O(n**2), best-case performance: O(n*log(n)).
Insertion sort worst-case performance: O(n**2), best-case performance: O(n).'''


# In[2]:


def insert_sort(lista):
    
    '''Insertion sort.
    
    Compares all the elements preceding the chosen element in the list. All the elements greater than the chosen element are moved after it.
    The operation is repeated for each element from the list.'''
    
    if type(lista) == list:
        
        n = len(lista)
        if n < 2:
            return lista
        else:
            for i in range(1, n):
                el = lista[i]
                j = i-1
                try:
                    
                    while j >= 0 and lista[j] > el:
                        lista[j+1] = lista[j]
                        j -= 1
                    lista[j+1] = el
                    
                except TypeError:
                        print('The list must contain numbers.')
                        return None
            return lista
    
    else:
        raise TypeError('The function argument must be a list containing numbers.')


# In[4]:


def choose_pivot(lista, l, h, pi):
    
    '''Chooses the reference element and moves it on the last place in the list.
    
    Options: first, last, middle, random.'''
    
    pivs = {'first': l, 'last': h, 'middle': (l+h)//2, 'random': random.randint(l, h)}
    pivot = lista[pivs[pi]]
    lista[pivs[pi]], lista[h] = lista[h], lista[pivs[pi]]
    
    return pivot, lista
   
    
def partition(lista, l, h, pi):
    
    '''Places the reference element on its right place in the sorted list.'''
    
    pivot, lista = choose_pivot(lista, l, h, pi)
    i = l-1
  
    for j in range(l, h): 
        if lista[j] <= pivot:   
            i += 1
            lista[i], lista[j] = lista[j], lista[i]  
    
    lista[i+1], lista[h] = lista[h], lista[i+1] 
    return i+1 


def quick_sort_rec(lista, l, h, pi, modif=False, mod_len=10):
    
    '''Sorts the list elements with the use of recursive version of quicksort algorithm.
    
    Places the reference element (pivot) on its right place in the sorted list. Repeats the operation untill the whole list is sorted'''
    
    if type(lista) == list:
        if len(lista) < 2:
            return lista
        else:
            try:
                if l < h: 
                    if modif and ((h-l) < mod_len):
                        lista = insert_sort(lista[l:h+1])


                    else:
                        try:
                            pi_ind = partition(lista, l, h, pi)
                        except KeyError:
                            print('Pivot options: first, last, middle, random.')
                            return None

                        if modif and ((pi_ind - l) < mod_len):
                            insert_sort(lista[l:pi_ind])
                        else:
                            quick_sort_rec(lista, l, pi_ind-1, pi)

                        if modif and ((h - pi_ind) < mod_len):
                            insert_sort(lista[pi_ind+1: h+1])
                        else:
                            quick_sort_rec(lista, pi_ind+1, h, pi)

                return lista
            except TypeError:
                print('The list must contain numbers.')
                return None
                
    else:
        raise TypeError('The function argument must be a list containing numbers.')

