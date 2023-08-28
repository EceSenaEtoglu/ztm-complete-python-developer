def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))

        except StopIteration:
            break

# for item in [1,2,100]:
#    print(item)
custom_for([1,2,100])