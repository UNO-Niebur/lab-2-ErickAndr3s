#Magic8Ball.py
#Name: Erick Andres
#Date: 30/01/2026
#Assignment:Lab 2
#purpose: The purpose of this program is to prompt the user for a question and display a randomly selected response using a list and the random.choice() function.

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  question = input ("Ask the magic 8 ball a question: ")
  #list of possible answers
  answers = ["It is certain", "It is decidedly to", "Without a doubt", "Yes definetly", "You may reply on it", "As I see it, yes", "Most likely", "Outlook good", 
            "Yes", "Signs point to yes", "Reply hazy, try again", "ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
             "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful" ]
  #Answer question randomly with one of the options from your earlier list.
  r = random.choice(answers)

  print(r)

if __name__ == '__main__':
  main()
