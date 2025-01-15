>>> import operator
>>> from functools import partial
>>> from first import first
>>> 
>>> first([-1, 0, 1, 2], key=partial(operator.le, 0))
0
>>> first([-1, 0, 1, 2], key=partial(operator.le, 2))
2
>>> first([0, False, None, [], (), 42])
42
>>> list(filter(lambda x: x > 0, [-1, 0, 1, 2]))[0]
1
>>> import itertools
>>> a = [{'foo': 'bar'}, {'foo': 'bar', 'x': 42}, {'foo': 'baz', 'y': 43}]
>>> a
[{'foo': 'bar'}, {'foo': 'bar', 'x': 42}, {'foo': 'baz', 'y': 43}]

>>> b=list(itertools.groupby(a, operator.itemgetter('foo')))
>>> b
[('bar', <itertools._grouper object at 0x10e86a5f8>), ('baz', <itertools._grouper object at 0x10e86a630>)]

>>> list(zip([1, 2, 3], ['a', 'b', 'c']))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> list(map(len, ['abc', 'de', 'fghi']))
[3, 2, 4]
>>> list(map(sum, zip([1, 2, 3], [4, 5, 6])))
[5, 7, 9]

>>> import itertools as it
>>> x = [1, 2, 3, 4, 5]
>>> y = ['a', 'b', 'c']
>>> list(zip(x, y))
[(1, 'a'), (2, 'b'), (3, 'c')]

>>> list(it.zip_longest(x, y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

>>> def grouper(inputs, n, fillvalue=None):
...     iters = [iter(inputs)] * n
...     return it.zip_longest(*iters, fillvalue=fillvalue)
... 
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(list(grouper(nums, 4)))
[(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, None, None)]

>>> bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
>>> list(it.combinations(bills, 3))
[(20, 20, 20), (20, 20, 10), (20, 20, 10), (20, 20, 10), (20, 20, 10), (20, 20, 10), (20, 20, 5), ...]

>>> list(it.combinations([1, 2], 2))
[(1, 2)]
>>> list(it.combinations_with_replacement([1, 2], 2)) # [(1, 1), (1, 2), (2, 2)]

>>> list(it.permutations(['a', 'b', 'c']))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

>>> counter = it.count()
>>> list(next(counter) for _ in range(5)) # [0, 1, 2, 3, 4]

>>> count_with_floats = it.count(start=0.5, step=0.75)
>>> list(next(count_with_floats) for _ in range(5))
[0.5, 1.25, 2.0, 2.75, 3.5]

>>> negative_count = it.count(start=-1, step=-0.5)
>>> list(next(negative_count) for _ in range(5))
[-1, -1.5, -2.0, -2.5, -3.0]

>>> list(zip(it.count(), ['a', 'b', 'c']))
[(0, 'a'), (1, 'b'), (2, 'c')]

>>> list(it.accumulate([1, 2, 3, 4, 5], operator.add)) # [1, 3, 6, 10, 15]
>>> list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y) / 2))
[1, 1.5, 2.25, 3.125, 4.0625]

>>> five_ones = it.repeat(1, 5)  # 1, 1, 1, 1, 1
>>> three_fours = it.repeat(4, 3)  # 4, 4, 4
>>> alternating_ones = it.cycle([1, -1]) 
>>> 

>>> it.product([1, 2], ['a', 'b'])  # (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')

>>> list(it.chain('ABC', 'DEF')) # ['A', 'B', 'C', 'D', 'E', 'F']

>>> list(it.chain([1, 2], [3, 4, 5, 6], [7, 8, 9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list(it.chain('abc', [1, 2, 3]))
['a', 'b', 'c', 1, 2, 3]

>>> list(it.chain.from_iterable([[1, 2, 3], [4, 5, 6]]))
[1, 2, 3, 4, 5, 6]
