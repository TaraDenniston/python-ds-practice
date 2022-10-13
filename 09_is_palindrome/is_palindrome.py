def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    new_phrase = phrase.lower().replace(" ", "")
    end_index = -1

    for x in range(len(new_phrase) // 2):
        if new_phrase[x] != new_phrase[end_index]:
            return False
        end_index -= 1      

    return True

