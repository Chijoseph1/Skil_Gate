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
    for index,question in enumerate(questions, start=1):
        print(f"Question {index} .{question["question"]}")
        for key,value in question["options"].items():
            print(f"{key}.{value}")

        while True:
            answer = input("Input answer(A-D): ").strip().upper()

            if answer in ["A","B","C","D"]:
                candidate_answer.append(answer)
                break
            else:
                print("Invalid answer. Please enter A, B, C, or D.")
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

def save_result(name,final_results,status):
    with open("assessment_result.txt","w") as file:
        file.write(f"Canditate Name:{name}\n")
        file.write(f"Final score:{final_results}/10\n")
        file.write(f"Status: {status}\n")
        file.write("--------------------------\n")

def view_result():
    with open("assessment_result.txt", "r") as file:
        content = file.read()
        print("\n========== ASSESSMENT RESULTS ==========")
        print(content)

def main():
    print("====================================")
    print("           SKILL-GATE              ")
    print("====================================")

    while True:
        print("you have been selected for an assessment\n")
        print("You will answer 10 questions.\n what will you like to do")

        print("\n1. Take Assessment")
        print("2. View Results")
        print("3. Exit")
        option = input("Choose an option (1-2): ""\n").strip()

        if option == "1":
            name = input("Enter your full name: ").strip()
            selected = select_question()
            answer =conduct_Assessment(selected)
            result, final_score, status = scoring(selected, answer)
            save_result(name,final_score,status)
            print("Thank you,Assessment completed successfully!")
            break
        elif option == "2" :
            while True:
                password = input("Input password to view result: ").strip()
                if check_result(password):
                    view_result()
                    break
                else:
                    print("Wrong password. Try again.")
            break
        else:
            print("Try again")

if __name__ == "__main__":
    main()