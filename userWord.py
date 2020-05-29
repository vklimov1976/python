# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Enter a word: ")
letters = "aeiouAEIOU"
uW = []

for letter in userWord:
    if letter not in letters:
        uW += letter
        uW = ''.join(uW)
print(uW)