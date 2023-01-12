
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
      "if it is to hear a joke, press 3 \n"
      "if you want to go home, press 4 \n")

while True:
    decision = float(input())
    int(decision)
    if decision == 1:
        print(" We used to think that the brain was fully developed by very early teenagerhood \n"
          " and we now realise that the brain doesn't stop developing until mid-20s or even \n"
          " early 30s. There's a lot more information and evidence to suggest that actually \n"
          " brain development in various forms goes on throughout the life span. \n")
    elif decision == 2:
        print("Read this book to learn programming: https://automatetheboringstuff.com/  \n")
    elif decision == 3:
        print("!false \n"
        "It's funny 'cause it's true. \n")
    elif decision == 4:
        break
    else:
        print("Please choose option: 1, 2, 3, or 4 \n")
    print("Anything else? ")

print("Thank you for coming, hope to see you soon :)")
