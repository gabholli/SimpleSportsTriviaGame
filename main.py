import random

import database


def sports_trivia_question_format(guess, answer):
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
    print("")
    print("Your score currently is: " + str(score))
    print("")


def input_prompt():
    answer = 0
    try:
        answer = int(input("Please select an answer: "))
    except ValueError:
        pass
    return answer


def multiple_choices(a, b, c, d):
    print("1: " + a)
    print("2: " + b)
    print("3: " + c)
    print("4: " + d)


def list_of_questions():
    questions = [
        "What MLB team has the record for most runs in a game(modern era)?",
        "What is the most popular sport in the world?",
        "When were the San Jose Sharks formed?",
        "Which of these years did the Houston Astros win the World Series?",
        "How many Super Bowls have the Texans won?"
    ]

    random.shuffle(questions)

    while len(questions):
        if questions[0] == "What MLB team has the record for most runs in a game(modern era)?":
            print("What MLB team has the record for most runs in a game(modern era)?")
            multiple_choices("Texas Rangers",
                             "Chicago Cubs", "Boston Red Sox", "New York Yankees")
            choice = input_prompt()
            sports_trivia_question_format(choice, 1)
            del questions[0]
        elif questions[0] == "What is the most popular sport in the world?":
            print("What is the most popular sport in the world?")
            multiple_choices("Baseball", "Basketball", "Soccer",
                             "Golf")
            choice = input_prompt()
            sports_trivia_question_format(choice, 3)
            del questions[0]
        elif questions[0] == "When were the San Jose Sharks formed?":
            print("When were the San Jose Sharks formed?")
            multiple_choices("2000", "1991", "1995", "1982")
            choice = input_prompt()
            sports_trivia_question_format(choice, 2)
            del questions[0]
        elif questions[0] == "Which of these years did the Houston Astros win the World Series?":
            print("Which of these years did the Houston Astros win the World Series?")
            multiple_choices("2005", "2017", "2000", "2020")
            choice = input_prompt()
            sports_trivia_question_format(choice, 2)
            del questions[0]
        elif questions[0] == "How many Super Bowls have the Texans won?":
            print("How many Super Bowls have the Texans won?")
            multiple_choices("One", "Five", "Two", "Zero")
            choice = input_prompt()
            sports_trivia_question_format(choice, 4)
            del questions[0]


def replay_prompt():
    yes_answer = "Y"
    no_answer = "N"
    while True:
        exit_prompt = input("Do you want to play again: Y or N: ")
        if exit_prompt == yes_answer:
            return yes_answer
        elif exit_prompt == no_answer:
            return no_answer
        elif exit_prompt != yes_answer or exit_prompt != no_answer:
            print("")
            print("Please make a valid entry")
            print("")
            continue


if __name__ == '__main__':
    while True:
        name_entered = input("Please Enter Your Name: ")
        database.create_table_queries()
        score = 0
        print("Welcome To The Sports Trivia Game!")
        print("----------------------------------")

        list_of_questions()

        print("Your final score is " + str(score) + "!")
        print("")
        database.add_db_row(name_entered, score)
        database.retrieve_current_high_score_by_name(name_entered)
        database.retrieve_high_scores_with_names()
        exit_answer = replay_prompt()
        if exit_answer == "Y":
            print("")
            continue
        elif exit_answer == "N":
            print("")
            print("Thank you for playing!")
            print("")
            input("Press Enter to close window:")
            break
