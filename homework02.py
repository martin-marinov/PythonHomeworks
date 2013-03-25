from collections import defaultdict, OrderedDict


def groupby(func, seq):
    result = defaultdict(list)
    for x in seq:
        result[func(x)].append(x)
    return result


def iterate(func):
    return accumulate(func, count)


def zip_with(func, *iterables):
    return (func(*ntuple) for ntuple in zip(*iterables))


def cache(func, cache_size):
    cached_args = OrderedDict()

    def func_cached(*args):
        cached_args[args] = func(*args)
        if len(cached_args) > cache_size:
            cached_args.popitem(last=False)
        return cached_args[args]
    return func_cached
