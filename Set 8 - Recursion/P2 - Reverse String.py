print('Reverse String')


def reverse(string):
    if len(string) == 0:
        return
    print(string[len(string) - 1], end="")
    return reverse(string[0:len(string) - 1])


string = 'afewewwefewb'
print(string[0:len(string) - 1])
print(string)
reverse('Hello')
print(string[1:len(string) - 1])
string = "hi"
print(string[1:len(string) - 1])