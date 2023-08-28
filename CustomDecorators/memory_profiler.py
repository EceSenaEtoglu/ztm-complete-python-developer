import psutil
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