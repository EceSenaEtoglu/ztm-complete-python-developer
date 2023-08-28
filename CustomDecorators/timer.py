import time
#timer template
def timer(func):
    def wrapper_func(*args,**kwargs):
        t1 = time.time()
        res = func(*args,**kwargs)
        t2 = time.time()-t1
        print(f"function {func.__name__} took {t2} seconds to run on inputs args: {args} kwargs: {kwargs}")
        return res
    return wrapper_func

@timer
def loop(loop_count):
    for i in range(loop_count):
        pass

loop(1000)
loop(100000)
loop(100000)