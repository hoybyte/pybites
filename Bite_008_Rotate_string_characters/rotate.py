# Bite 8 - Rotate String characters

def rotate(string, n):
    """ Rotate characters in a string.
        Expects a string and n (int) for a number of characters to move.
    """
    return string[n:] + string[:n]
