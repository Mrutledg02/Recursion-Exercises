"""Print each square on a new line.

A simple square will only be one line::

    >>> dump(0)
    0

    >>> dump(1)
    1

A split square will use four lines::

    >>> dump([0, 1, 0, 1])
    0
    1
    0
    1

A nested split square will use one line per square::

    >>> dump([0, 0, 0, [1, 1, 1, 1]])
    0
    0
    0
    1
    1
    1
    1

Of course, these can nested deeply and still work::

    >>> dump([0, 0, 0, [1, 1, 1, [0, 0, 0, [1, 1, 1, 1]]]])
    0
    0
    0
    1
    1
    1
    0
    0
    0
    1
    1
    1
    1
"""


def dump(s):
    """Print each square on a new line."""
    if isinstance(s, int):
        # If `s` is a simple square (0 or 1), print it.
        print(s)
    else:
        # `s` is a split square, which is a list of squares
        for square in s:
            dump(square) # Recursively print each sub-square

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASS; NICE JOB!\n")
