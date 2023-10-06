
cached_data = dict()

def cached(fn_target):

    def inner(*args, **kwargs):
        global cached_data

        if args[0] in cached_data:
            result = cached_data[args[0]]
        else:
            result = fn_target(*args, **kwargs)
            cached_data[args[0]] = result
        return result

    return inner