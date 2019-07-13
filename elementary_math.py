import random
import operator
correct_ans = 0
questions = 0
wrong_ans = []


def elementary_math():
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    global correct_ans
    global questions
    global wrong_ans
    questions += 1
    signs = {"+": operator.add, "-": operator.sub,
             "*": operator.mul}
    rnd_opr = random.choice(list(signs.keys()))
    art_qs = f"{a} {rnd_opr} {b} = "
    print(art_qs + "?")
    ans = signs[rnd_opr](a, b)
    user_ans = int(input("enter your enswer: "))
    yes_list = ["yes", "Yes", "y", "Y"]
    no_list = ["no", "No", "n", "N", ""]

    art_qs = f"{a} {rnd_opr} {b} = {ans} ({user_ans}) "
    if user_ans == ans:
        correct_ans += 1
        print("correct answer")
        user_selct = input("do you like play again? :")
        if user_selct in yes_list:
            elementary_math()
        if user_selct in no_list:
            for x in wrong_ans:
                print(x)
    else:
        wrong_ans.append(art_qs)
        print("wrong answer")
        user_selct = input("do you like play again? :")
        if user_selct in yes_list:
            elementary_math()
        if user_selct in no_list:
            for x in wrong_ans:
                print(x)
    return f"You have answered correctly {correct_ans} out of {questions} problems"


x = elementary_math()

print(x)
