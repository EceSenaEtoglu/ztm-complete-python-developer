new_list = list(range(1000))
print(new_list)

def make_list(num):
    empty_list = []
    for i in range(num):
        empty_list.append(i)
    return empty_list

#code above is equivalent to the first statement, stores additional list on memory
#instead use generators and return numbers 'one by one' to print them

#generator template
def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(1000):
    print(item)

#generator = generator_function(1000)
#next(generator)
#next(generator)
#print(next(generator))