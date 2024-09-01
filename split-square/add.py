"""Produce new square adding two inputs squares.

Two simple squares can be added::

    >>> s1 = 0
    >>> s2 = 1

    >>> add(s1, s2)
    1

A simple square and a split square can be added::

    >>> s1 = 0
    >>> s2 = [1, 0, 1, 0]

    >>> add(s1, s2)
    [1, 0, 1, 0]

Two split squares can be added::

    >>> s1 = [0, 0, 0, 1]
    >>> s2 = [0, 1, 0, 1]

    >>> add(s1, s2)
    [0, 1, 0, 1]

Nested squares can be added::

    >>> s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

Unevenly-nested squares can be added::

    >>> s1 = [0, [1, 1, 1, 0           ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> s1 = [0, [1, 1, 1, 1                      ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
"""


def add(s1, s2):
    """Produce new split square adding two input squares."""

    # Helper function to add two parts
    def add_parts(p1, p2):
        if isinstance(p1, int) and isinstance(p2, int):
            # Both are simple squares
            return 1 if p1 == 1 or p2 == 1 else 0
        elif isinstance(p1, list) and isinstance(p2, list):
            # Both are split squares
            return [add_parts(x1, x2) for x1, x2 in zip(p1, p2)]
        else:
            # Handle cases where one is a simple square and the other is a split square
            if isinstance(p1, int):
                return add_parts([p1, p1, p1, p1], p2) # Convert simple to split
            else: 
                return add_parts([p1, [p2, p2, p2 ,p2]]) # Convert simple to split
            
    return add_parts(s1, s2)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASS; YOU'RE A RECURSION WIZARD!\n")
