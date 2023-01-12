
print("Hello, please insert your name: ")
name = input()

print("Nice to meet you " + name + ", I am Carpton \n" \
       "Please tell me your age: ")
while True:
    age = float(input())
    if age >= 18 > 0:
        print("Access Granted")
        break
    elif 0 < age < 18:
        print("Sorry you are underage ")
        continue
    else:
        print("Please provide a valid number")
        continue

print("Please tell me the destination of your journey \n"
      "if it is to hear a fun fact, press 1 \n"
      "if it is to learn, press 2 \n"
      "if it is to hear a joke press 3")
decision = int(input())
while True:
    if decision == 1:
        print("We used to think that the brain was fully developed by very early teenagerhood \n"
          " and we now realise that the brain doesn't stop developing until mid-20s or even \n"
          " early 30s. There's a lot more information and evidence to suggest that actually \n"
          " brain development in various forms goes on throughout the life span. \n")
        break
    elif decision == 2:
        print("Read this book to learn programming: https://automatetheboringstuff.com/  \n")
        break
    elif decision == 3:
        print("!false \n"
        "It's funny 'cause it's true. \n")
        break
    else:
        print("please provide a number between 1 and 3")

print("Thank you for coming, hope to see you soon :)")


