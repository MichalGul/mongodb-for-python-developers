from collections.abc import Iterable


def multiziperator(*iterables):
    if any([not isinstance(arg, Iterable) for arg in iterables]):
        raise StopIteration("All data provided must be Iterable")

    # Gather iterator list from iterables
    iterators = [iter(it) for it in iterables]

    # iterate over objects iterators
    while iterators:
        iters_results = []
        for it in iterators:
            elem = next(it, False)
            iters_results.append(elem)
        # check if all iterators returns proper value
        if all(iters_results):
            for e in iters_results:
                yield e
        # otherwise stop iteration at shortest iterable
        else:
            return



# multiziperator([1,2,3], "AVSD", 5)
# a = list(multiziperator("abc", [1,2,3], "zx"))
# print(a)
#
for one_item in multiziperator("abc", [1,2,3], "zx", [3,4,5], "dup"):
    print(one_item)
