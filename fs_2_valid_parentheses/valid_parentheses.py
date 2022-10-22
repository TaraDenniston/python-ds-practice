def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    if len(parens) % 2 == 0:
        if parens[0] == '(' and parens[-1] == ')':
            for i in range(1, len(parens) - 1):
                if parens[i] == '(' and parens[-i - 1] == ')' or \
                   parens[i] == ')' and parens[-i - 1] == '(':
                   continue
                else:
                    return False
        else:
            return False
    else:
        return False 

    return True

