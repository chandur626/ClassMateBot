# About $sentiment
This command analyzes the sentiment of the message in the context. It returns the polarity score of the message. 

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/chandur626/ClassMateBot/blob/main/cogs/SentimentAnalysis.py)

# Code Description
## Functions
on_message(self, message): <br>
This function takes self and message as the arguments. It then stores the message in a variable called self.mess for other functions to access it. 

sentiment(self, ctx): <br>
This function takes self and ctx as the arguments. It then takes the value of self.message and analyzes the sentiment of the same. It then returns the sentiment and polarity of the message. 

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter your message and enter the command '$sentiment'.
```
your message
$sentiment
```
Successful execution of this command will return a the sentiment of the message and its polarity score.

![$sentiment HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/SentimentAnalysis.gif)