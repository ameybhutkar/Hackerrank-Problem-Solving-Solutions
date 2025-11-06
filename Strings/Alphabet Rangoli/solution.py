def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    # Create a list to hold each line of the rangoli
    lines = []

    # Build the top half including the middle
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size - 3, "-"))

    # Print the full rangoli (top + reversed bottom)
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
