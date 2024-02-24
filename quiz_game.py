print("**********Welcome to Computer quiz game!**********")

game_end = False

while not game_end:
    playing = input("Do you want to play? [yes/no] ").lower()

    if playing != "yes":
        quit()
    print()
    print("**********You must score 7 out of 10 to pass the quiz**********")
    print()
    score = 0

    question_set = ["What is the full form of RAM?", 
                    "What is the full form of CPU?", 
                    "What is the full form of GPU?", 
                    "What is the full form of HDD?", 
                    "What is the full form of SSD?", 
                    "What is the full form of BIOS?", 
                    "What is the full form of USB?", 
                    "What is the full form of LAN?", 
                    "What is the full form of WAN?", 
                    "What is the full form of IP?"]
    answer_set = ["random access memory", 
                "central processing unit", 
                "graphics processing unit", 
                "hard disk drive", 
                "solid state drive", 
                "basic input output system", 
                "universal serial bus", 
                "local area network", 
                "wide area network", 
                "internet protocol"]

    from random import randint

    for i in range(len(question_set)):    # 0 - 9
        random_number = randint(0, (len(question_set)-1))     # 0 - 9

        answer = input(question_set[random_number] + " ").lower()

        if answer == answer_set[random_number]:
            print("Correct!")
            score += 1
            question_set.remove(question_set[random_number])
            answer_set.remove(answer_set[random_number])
        else:
            print("Incorrect")

    print("*"*30)
    print("Your Score:", score)
    if score >= 7:
        print("you cleared the test :) ")
        game_end = True
    else:
        print("Better luck next time!")
        print()
        game_end = False
        print("Its advisable to play the game again, ", end="")