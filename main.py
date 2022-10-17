def sportsTriviaQuestions(guess, answer):
    global score
    isGuessing = True
    while isGuessing:
        if guess == answer:
            print("Correct Answer")
            score += 1
            isGuessing = False
        else:
            print("Incorrect Answer!")
            break
    print("Your score currently is: " + str(score))

def inputPrompt():
    answer = 0
    try:
        answer = int(input("Please select an answer: "))
    except ValueError:
        pass
    return answer

def multipleChoices(question, a, b, c, d):
    print(question)
    print("1: " + a)
    print("2: " + b)
    print("3: " + c)
    print("4: " + d)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score = 0
    print("Welcome To The Sports Trivia Game!")
    print("----------------------------------")

    print("")


    multipleChoices("What number equals one?", "One", "Two", "Three", "Four")
    promptValue = inputPrompt()
    sportsTriviaQuestions(promptValue, 1)
    multipleChoices("What number equals two?", "One", "Two", "Three", "Four")
    promptValueTwo = inputPrompt()
    sportsTriviaQuestions(promptValueTwo, 2)
    multipleChoices("What number equals three?", "One", "Two", "Three", "Four")
    promptValueThree = inputPrompt()
    sportsTriviaQuestions(promptValueThree, 3)
    multipleChoices("What number equals four?", "One", "Two", "Three", "Four")
    promptValueFour = inputPrompt()
    sportsTriviaQuestions(promptValueFour, 4)
