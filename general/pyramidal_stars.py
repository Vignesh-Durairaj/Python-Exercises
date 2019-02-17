def print_left_pyramidal_stars(num):
    for i in range(1, num + 1):
        print('*' * i)


def print_right_pyramidal_stars(num):
    val = 1
    for i in reversed(range(1, num + 1)):
        space = ''
        for j in range(i):
            space += ' '
        print(space + ('*' * val))
        val += 1


def print_pyramidal_stars(num):
    val = 1
    for i in reversed(range(1, num + 1)):
        space = ''
        for j in range(i // 2):
            space += ' '
        space += ' ' if i % 2 != 0 else ''
        print(space + ('*' * val))
        val += 1


print_right_pyramidal_stars(19)
print_left_pyramidal_stars(19)
print_pyramidal_stars(19)
