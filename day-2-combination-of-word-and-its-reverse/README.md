# Day 2 - Combo of a Given Word + Its esreveR

## Prompt

Write a function called `fun_with_words(word)` that takes as input a word (string) and returns a new word that is a combination of the given word and of its reverse. For example, calling `fun_with_words('TrAvElInGpRoGrAmMeR')`, one should get the following output `'TrAvElInGpRoGrAmMeRReMmArGoRpGnIlEvArT'`. If you are not a beginner, write an additional function called `fun_with_words2(word)` that does the same but also removes all vowels from the resulting string.

## Solution

### B E G I N N E R
Once you create the function, you only need to return the word (as `word`) + `word[::-1]`


### A D V A N C E D
You will need to return your new word, so we must define it first as a paramenter

`new_word = fun_with_words(word)`

Then we need to take every vowel (both upper and lower case) and replace them:

for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
  new_word = new_word.replace(vowel, '')

Then we return the `new_word` from above


Here's an [example](https://stackoverflow.com/questions/7301292/string-replace-vowels-in-python) from our good friends at stackoverflow.com:

| code | documentation
|:---|:---|
|def removeVowels(word):|
|.....letters = [] | # make an empty list to hold the non-vowels|
|.....for char in word: | # for each character in the word|
|..........if char.lower() not in 'aeiou':| # if the letter is not a vowel|
|...............letters.append(char) | # add it to the list of non-vowels|
|.....return ''.join(letters) | # join the list of non-vowels together into a string|

