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

    multiple_choices("Which of these years did the Houston Astros win the World Series?",
                     "2005", "2017", "2000", "2020")
    prompt_value_four = input_prompt()
    sports_trivia_questions(prompt_value_four, 2)

    multiple_choices("How many Super Bowls have the Texans won?", "One", "Five", "Two", "Zero")
    prompt_value_five = input_prompt()
    sports_trivia_questions(prompt_value_five, 4)


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
            continue
        elif exit_answer == "N":
            print("")
            print("Thank you for playing!")
            input("Press Enter to close window:")
            break
