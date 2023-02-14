import random
name=input("Hello! What is your name?\n")
print("Well, %s, I am thinking of a number between 1 and 20." % name)
sol=random.randint(1, 20)
n=int(input("Take a guess.\n"))
cnt=1
while n!=sol:
    if n<sol:
        print("Your guess is too low.")
    elif n>sol:
        print("Your guess is too high.")
    n=int(input("Take a guess.\n"))
    cnt+=1
print("Good job, %s! You guessed my number in %d guesses!" % (name, cnt))
