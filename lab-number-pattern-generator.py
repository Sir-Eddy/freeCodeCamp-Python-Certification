def number_pattern(n):
    number = 1
    number_list = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    while number <= n:
        number_list += str(number)
        number_list += ' '
        number += 1
    number_list = number_list[:-1]
    return number_list


print(number_pattern(4))
