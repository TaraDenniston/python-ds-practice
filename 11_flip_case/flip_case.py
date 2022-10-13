def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # phrase_lst = [char for char in phrase]

    # print(phrase_lst)

    new_phrase = ''
    
    for char in phrase:
        if char.lower() == to_swap.lower():
            new_phrase += char.swapcase()
        else:
            new_phrase += char

    return new_phrase
