# Day 4 - Check the Conditions of an Insta Handle (Good or Bad)

## Prompt

Write a function called `check_insta_handle(name)` that takes as input a name (string), and returns 'Good' if the handle is a good choice and 'Bad' otherwise. Let's define what a 'Good' insta handle is:
-No underscores,
-No hyphens,
-No dots at the beginning or at the end of the name,
-Not too long, 20 characters max.

**If you are advanced**, write an additional function called `check_insta_handle2` that does the same as the previous one but also includes the following conditions:
-Not a combination of uppercase and lowercase letters (all letter uppercase or all lowercase),
-No digits,
-No following special characters: `@!#$%^&*?~:`.

## Solution

### B E G I N N E R

There are 4 things we need to look out for:

   *  #1: No underscores: `'_' not in name`
   *  #2: No hyphens: `'-' not in name`
   *  #3: No dots at beginning or end of name: `len(name)<=20`
   *  #4: 20 characters max: `not name.startswith('.'), not name.endswith('.')`

We get this function started by using `if all` because we want these 4 conditions to be checked for all inputs.

This way we'll want to return something saying "if all these things don't apply....return `Good`" .... else: return `Bad`

### A D V A N C E D

