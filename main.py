import random

import database


def sports_trivia_question_format(guess, answer):
    global score
    is_guessing = True
    while is_guessing:
        if guess == answer:
            print("Correct Answer!")
            score += 1
            is_guessing = False
        else:
            print("Incorrect Answer!")
            break
    print("")
    print("Your score currently is: " + str(score))
    print("")


def input_prompt():
    answer = input("Please type your answer: ")
    return answer


def list_of_questions():
    quiz_questions = [
        ["What MLB team has the record for most runs in a game(modern era)?", "Texas Rangers"],
        ["What is the most popular sport in the world?", "Soccer"],
        ["In what year were the San Jose Sharks formed?", "1991"],
        ["Did the Houston Astros win the World Series in 2017?", "Yes"],
        ["What NHL team does Connor McDavid play for in the 2022-2023 season?", "Edmonton Oilers"],
        ["What year was the Chase Center of the Golden State Warriors opened?", "2019"],
        ["How many NHL teams get to go to the playoffs in 2023?", "16"],
        ["Are the Houston Nachos a real football team?", "No"],
        ["What is the most popular sport in Canada?", "Hockey"]
    ]

    random.shuffle(quiz_questions)

    for i in range(len(quiz_questions)):
        print(quiz_questions[i][0])
        choice = input_prompt()
        sports_trivia_question_format(choice, quiz_questions[i][1])


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


def run_quiz():
    global score
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


if __name__ == '__main__':
    score = 0
    run_quiz()
