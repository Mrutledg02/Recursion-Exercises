"""Simplify a split square:

A simple square is already simplified::

    >>> simplify(0)
    0

A split square containing four simple filled squares can be
simplified to a simple filled square::

    >>> simplify([1, 1, 1, 1])
    1

A split square containing four simple empty squares can be
simplified to a simple empty square::

    >>> simplify([0, 0, 0, 0])
    0

A split square containing mixed squares cannot be simplified::

    >>> simplify([1, 0, 1, 0])
    [1, 0, 1, 0]

These can be simplified even when nested::

    >>> simplify([1, 0, 1, [1, 1, 1, 1]])
    [1, 0, 1, 1]

Simplification should nest, so if we can simplify one split square
into a simple square and now an outer split square can be
simplified, it should::

    >>> simplify([1, 1, 1, [1, 1, 1, 1]])
    1

    >>> simplify([[1, 1, 1, 1], [1, 1, 1, 1], 1, 1])
    1

    >>> simplify([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1])
    [1, 0, [1, 0, 1, 1], 1]

Be careful that we don't "simplify" a set of matching mixed squares:

    >>> simplify([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]])
    [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
"""


def simplify(s):
    """Simplify a split square."""
    
    # Helper function to simplify individual parts
    def simplify_part(part):
        if isinstance(part, list):
            return simplify(part)
        return part
    
    # Check if s is a simple square
    if isinstance(s, int):
        return s
    
    # Check if s is a split square
    if isinstance(s, list) and len(s) == 4:
        simplified_parts = [simplify_part(part) for part in s]
        
        # Check if all parts are the same and are simple squares
        if (simplified_parts[0] == simplified_parts[1] == simplified_parts[2] == simplified_parts[3] and isinstance(simplified_parts[0], int)):
            return simplified_parts[0]
        
        # Otherwise, return the split square with simplified parts
        return simplified_parts
    
    # If s is neither a simple square nor a valid split square
    return s

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASS; YOU MADE THAT SEEM SIMPLE!!\n")
