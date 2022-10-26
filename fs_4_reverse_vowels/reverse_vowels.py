def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    
    new_s = ''

    # turn string into dictionary using index numbers as keys
    s_dict = dict(enumerate(s))

    # extract all key/value pairs that contain a vowel
    vowels = {k:v for (k,v) in s_dict.items() if v in 'AaEeIiOoUu'}

    # separate key/value pairs into two lists, reverse the order of the vowels, 
    # and put them back together into a dictionary
    keys = list(vowels.keys())
    values = list(vowels.values())
    values = values[::-1]
    vowels = dict(zip(keys, values))

    # update original dictionary with the new order of vowels
    s_dict.update(vowels)

    # turn dictionary back into string
    for val in s_dict.values():
        new_s += val

    return new_s

