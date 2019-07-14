import random
import operator
correct_ans = 0
questions = 0
wrong_ans = []


def get_rnd_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    signs = {"+": operator.add, "-": operator.sub,
             "*": operator.mul}
    rnd_opr = random.choice(list(signs.keys()))
    art_qs = f"{a} {rnd_opr} {b} = "
    print(art_qs + "?")
    ans = signs[rnd_opr](a, b)
    return ans, art_qs


def math_quiz():

    global correct_ans
    global questions
    global wrong_ans
    questions += 1
    ans_art_qs_tupple = get_rnd_question()
    ans = ans_art_qs_tupple[0]
    art_qs = ans_art_qs_tupple[1]
    user_ans = int(input("enter your enswer: "))
    yes_list = ["yes", "Yes", "y", "Y"]
    no_list = ["no", "No", "n", "N", ""]

    art_qs = art_qs + f"{str(ans)} ({str(user_ans)})"
    if user_ans == ans:
        correct_ans += 1
        print("correct answer")
        user_selct = input("do you like play again? :")
        if user_selct in yes_list:
            math_quiz()
        if user_selct in no_list:
            print("this are all your incorrect questions:")
            for x in wrong_ans:
                print(x)
    else:
        wrong_ans.append(art_qs)
        print("wrong answer")
        user_selct = input("do you like play again? :")
        if user_selct in yes_list:
            math_quiz()
        if user_selct in no_list:
            print("this are all your incorrect questions:")
            for x in wrong_ans:
                print(x)
    return f"You have answered correctly {correct_ans} out of {questions} problems"


x = math_quiz()

print(x)
