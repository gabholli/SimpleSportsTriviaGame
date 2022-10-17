
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
    print("")


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


if __name__ == '__main__':


    score = 0
    print("Welcome To The Sports Trivia Game!")
    print("----------------------------------")

    print("")


    multipleChoices("What MLB team has the record for most runs in a game(modern era)?", "Texas Rangers",
                    "Chicago Cubs", "Boston Red Sox", "New York Yankees")
    promptValue = inputPrompt()
    sportsTriviaQuestions(promptValue, 1)
    multipleChoices("What is the most popular sport in the world?", "Baseball", "Basketball", "Soccer", "Golf")
    promptValueTwo = inputPrompt()
    sportsTriviaQuestions(promptValueTwo, 3)
    multipleChoices("When were the San Jose Sharks Formed?", "2000", "1991", "1995", "1982")
    promptValueThree = inputPrompt()
    sportsTriviaQuestions(promptValueThree, 2)
    print("Your final score is " + str(score) + "!")
