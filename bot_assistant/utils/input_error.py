def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass

    return inner
