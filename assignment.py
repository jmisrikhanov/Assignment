answer = 'Javid'

question = 'What is your name?  '
print ("Let's find the password!")

while True:
    guess = str(input(question))
    if guess == answer:
        print("Hello, Joseph! The password is : W@12")
    else: 
        print("Hello, Amina! See you later.") 
    break
