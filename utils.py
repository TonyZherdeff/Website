def odd_list_create(num_start, num_end) -> str:
    odd_list = []
    i = num_start
    while i <= num_end:
        if i % 2:
            odd_list.append(str(i))
        i += 1
    return " ".join(odd_list)


def even_list_create(num_start, num_end) -> str:
    even_list = []
    i = num_start
    while i <= num_end:
        if not i % 2:
            even_list.append(str(i))
        i += 1
    return " ".join(even_list)


def simple_list_create(num_start, num_end) -> str:
    simple_list = []
    i = num_start
    while i <= num_end:
        if is_prime(i):
            simple_list.append(str(i))
        i += 1
    return " ".join(simple_list)


def square_list_create(num_start, num_end) -> str:
    square_list = []
    i = num_start
    while i <= num_end:
        square_list.append(str(i*i))
        i += 1
    return " ".join(square_list)


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True