## Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

## Use the Parameter Testing feature in the box below to test your code with different arguments.


def FirstReverse(str):

    return ''.join(reversed(str))

# keep this function call here
print FirstReverse(raw_input())