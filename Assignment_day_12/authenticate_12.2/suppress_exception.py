
def supress_exception(exception=None, result=None):
    def decorator(fn_target):
        def inner(*args, **kwargs):
            try:
                r = fn_target(*args, **kwargs)
            except Exception as e:
                if e == exception:
                    r = result
                else:
                    pass
            return r    
        return inner

    return decorator