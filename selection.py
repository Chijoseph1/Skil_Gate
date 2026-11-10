from question import get_questions
import random

def select_question():
    question = get_questions()
    selected = random.sample(question,10)
    return selected

def main():
    print("====================================")
    print("           SKILL-GATE              ")
    print("====================================")

    while True:
        print("you have been selected for an assessment\n")
        print("You will answer 10 questions.\n")

        option = input("Choose an option (1-2): ").strip()

        if option == "1":
            selected = select_question()
            print(selected)
        elif  option == "2":
            break
        else :
            print("TRy again")

if __name__ == "__main__":
    main()