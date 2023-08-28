#map
#filter
#zip
#reduce
import random
from functools import reduce

from typing import Tuple

entries = ["eceskskff", "senafkfff", "veliff"]

def jumble(word):
    lst = list(word)
    random.shuffle(lst)
    return "".join(lst)

def more_than_8_chars(password):
    return len(password) > 8


password_list = list(map(jumble,entries))
print(password_list)
print(entries)
valid_passwords_list = list(filter(more_than_8_chars,password_list))
print(valid_passwords_list)

lst1 = [1,2,3]
lst2 = [2,4,6]
lst3 = [4,6,8]
print(list(zip(lst1,lst2,lst3)))

def accumulator(acc,item):
    print(acc,item)
    #f(x)
    return acc + item

#used instead of explicit for loop, reduces the list
#not readable rather use built in sum for readbility and efficiency
print(reduce(accumulator,lst1,0))

#filter using lambda
print(list(filter(lambda x: len(x)>10,password_list)))


lst = [(0,1),(0,2),(9,-4)]
lst.sort(key = lambda my_tuple:my_tuple[1])

#comprehensions
#x = [param for param in iterable]
#list,set
even_list = [i for i in range(100) if i %2 == 0]
odd_set = {2*i+1 for i in even_list}

#dictionary comprehension
dict = {1:2,2:4}
square_dict = {key: value ** 2 for key,value in dict.items()}
print(square_dict)

new_dict = {item:item*2 for item in [1,2,3]}
print(new_dict)