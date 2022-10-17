import database


def sports_trivia_questions(guess, answer):
    global score
    is_guessing = True
    while is_guessing:
        if guess == answer:
            print("Correct Answer")
            score += 1
            is_guessing = False
        else:
            print("Incorrect Answer!")
            break
    print("Your score currently is: " + str(score))
    print("")


def input_prompt():
    answer = 0
    try:
        answer = int(input("Please select an answer: "))
    except ValueError:
        pass
    return answer


def multiple_choices(question, a, b, c, d):
    print(question)
    print("1: " + a)
    print("2: " + b)
    print("3: " + c)
    print("4: " + d)


def list_of_questions():
    multiple_choices("What MLB team has the record for most runs in a game(modern era)?", "Texas Rangers",
                     "Chicago Cubs", "Boston Red Sox", "New York Yankees")
    prompt_value = input_prompt()
    sports_trivia_questions(prompt_value, 1)

    multiple_choices("What is the most popular sport in the world?", "Baseball", "Basketball", "Soccer", "Golf")
    prompt_value_two = input_prompt()
    sports_trivia_questions(prompt_value_two, 3)

    multiple_choices("When were the San Jose Sharks formed?", "2000", "1991", "1995", "1982")
    prompt_value_three = input_prompt()
    sports_trivia_questions(prompt_value_three, 2)


if __name__ == '__main__':
    name_entered = input("Please Enter Your Name: ")
    database.create_table_queries()
    score = 0
    print("Welcome To The Sports Trivia Game!")
    print("----------------------------------")

    list_of_questions()

    print("")
    print("Your final score is " + str(score) + "!")
    database.add_db_row(name_entered, score)
    database.retrieve_high_scores_with_names()
