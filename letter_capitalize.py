#Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.

def LetterCapitalize(str):

  # in python there is a function called title which is
  # easier than using a regex pattern
  return str.title()


# keep this function call here
print LetterCapitalize(raw_input())
