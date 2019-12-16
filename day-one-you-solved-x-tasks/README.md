# Day 1 - Dear {}, you solved {} tasks!

## Prompt

Write a function called **`text_message(name,n)`** that takes as arguments a name (string) and a number of days participated in the challenge (int), and returns a personalized message: "Dear ..., you solved ... tasks.". For example, if John solved only 5 tasks and then gave up, the function should return "Dear John, you have solved 5 tasks so far.".
If you are quite advanced, extend this function so that it takes one additional argument called last_access_timestamp and for a sample input ('John', 5, datetime.datetime(2019,12,6,8,56,1)) returns the following message "Dear John, your participation rate was 20.8% and your last access was on 06-12-2019 at 08:56:01 AM." (the participation rate is just 5/24 rounded to one decimal place). Ideally, your updated function should have the date parameter specified as None by default so that it matches both input types!

<span style="color:red">some **This is Red Bold.** text</span>
