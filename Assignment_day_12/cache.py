
def cached(fn_target):
    cached_data = dict()
    def inner(*args, **kwargs):

        if args[0] in cached_data:
            result = cached_data[args[0]]
        else:
            result = fn_target(*args, **kwargs)
            cached_data[args[0]] = result
        return result

    return inner