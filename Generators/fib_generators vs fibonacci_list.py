import time
import psutil

#decorators to profile the functions
def memory_profiler(func):
    def wrapper_func(*args,**kwargs):
        process = psutil.Process()
        initial_mem = process.memory_info().rss
        func(*args, **kwargs)
        res = func(*args,**kwargs)
        mem_used = process.memory_info().rss - initial_mem
        print(f"function {func.__name__} took {mem_used / (2**20)} mb memory  on inputs args: {args} kwargs: {kwargs}")
        return res
    return wrapper_func


def timer(func):
    def wrapper_func(*args,**kwargs):
        t1 = time.time()
        res = func(*args,**kwargs)
        t2 = time.time()-t1
        print(f"function {func.__name__} took {t2} seconds to run on inputs args: {args} kwargs: {kwargs}")
        return res
    return wrapper_func

def fibonacci_generator(n):
    first = 0
    second = 1
    while n >= 0:
        yield first
        first, second = second, second + first
        n = n - 1


def fibonacci_list(n):
    first = 0
    second = 1
    fib_list = []
    while n >= 0:
        fib_list.append(first)
        first,second = second, first + second
        n -= 1
    return fib_list

@memory_profiler
def assign_with_generator(n):
    fib = fibonacci_generator(n)

@memory_profiler
def assign_with_list(n):
    fib = fibonacci_list(n)

assign_with_generator(20)
assign_with_list(20)

assign_with_generator(100000)
assign_with_list(100000)