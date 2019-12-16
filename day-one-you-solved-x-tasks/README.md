# Day 1 - Dear {}, you solved {} tasks!

## Prompt

Write a function called `text_message(name,n)` that takes as arguments a name (string) and a number of days participated in the challenge (int), and returns a personalized message: "Dear ..., you solved ... tasks.". For example, if John solved only 5 tasks and then gave up, the function should return "Dear John, you have solved 5 tasks so far.".

If you are quite advanced, extend this function so that it takes one additional argument called `last_access_timestamp` and for a sample input `('John', 5, datetime.datetime(2019,12,6,8,56,1))` returns the following message "Dear John, your participation rate was 20.8% and your last access was on 06-12-2019 at 08:56:01 AM." (the participation rate is just 5/24 rounded to one decimal place). Ideally, your updated function should have the date parameter specified as None by default so that it matches both input types!

## Solution

### B E G I N N E R
As you define `text_message(name,n)` you want to return the message with placeholders for the two variables: **name** and **number of tasks solved**. Because this is two variables and not three (not a tuple), we don't need to define them. You use `{}` to differentiate where the variables would go. The return becomes the *Formula* that will then be aligned with print (where the inputs are displayed).

With the `print` function, you put into the function: `John` and `5`. When you run your code, you will see that Python printed "Dear John, you have solved 5 tasks so far."

### A D V A N C E D

Before you define the function, you must `import datetime` to bring in the date and time relative to what you will be running.

We know that *Participation Rate* = 5 / 24 x 100, so we must write that as a parameter.

We'll return with placeholders `{}` for each of these three placeholders: `name`, `n`, and `last_access_timestamp`. This will yield for us: 

Dear {}, your participation rate was {}% \ and your last access was on {} at {}""".format(name, str(round(percentage, 1))
  last_access_timestamp.strftime("%d-%m-%Y"), 
  last_access_timestamp.strftime("%I:%M:%S %p")))

Write in: result = text_message_advanced("John", float(5), datetime.datetime(2019,12,6,8,56,1))

And then print:
print(result)
