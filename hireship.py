from question import get_questions
import random
import os
from dotenv import load_dotenv
load_dotenv()
admin_password = os.getenv("ROLEREADY_ADMIN_PASSWORD")

def select_question():
    question = get_questions()
    selected = random.sample(question,10)
    return selected

def conduct_Assessment(questions):
    candidate_answer =[]
    for question in questions:
        print(question["question"])
        for key,value in question["options"].items():
            print(f"{key}.{value}")
        answer = input("Input answer: ").strip().upper()
        candidate_answer.append(answer)
        print("Your answer has been successfully recorded!\n")
    return candidate_answer

def scoring(questions, candidate_answer):
    result = []

    for question, candidate in zip(questions, candidate_answer):
        correct = question["answer"]

        if correct == candidate:
            result.append({
                "candidate": candidate,
                "correct": correct,
                "result": "Correct"
            })
        else:
            result.append({
                "candidate": candidate,
                "correct": correct,
                "result": "Incorrect"
            })

    final_score = sum(
        1 for item in result if item["result"] == "Correct"
    )

    if final_score >= 7:
        status = "Qualified"
    elif final_score >= 5:
        status = "Needs Further Assessment"
    else:
        status = "Not Qualified"
    return result, final_score, status

def check_result(password):
    if password != admin_password:
        return False
    return True

    
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
            answer =conduct_Assessment(selected)
            result, final_score, status = scoring(selected, answer)
            
            while True:
                password = input("Input password to view result: ").strip()

                if check_result(password):
                    print(f"Final Score: {final_score}/10")
                    print(f"Status: {status}")
                    break
                else:
                    print("Wrong password. Try again.")
            break
        elif option == "2" :
            break
        else:
            print("Try again")

if __name__ == "__main__":
    main()