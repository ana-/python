# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

#Use the Parameter Testing feature in the box below to test your code with different arguments.

def LetterChanges(str):


  newString = ""

  for char in str:

    if char.isalpha():

      # check if character is z
      if char.lower() == 'z':
        char = 'a'

        char = chr(ord(char) + 1)

    if char in 'aeiou':
      char = char.upper()

    newString = newString + char

  return newString
