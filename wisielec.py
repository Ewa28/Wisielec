import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Gra w wisielca")

    while wrong < len(stages)-1 :
        if "_" in board:
            print("")
            msg = "Odgadnij literę "
            char = input(msg)
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
                print("Hasło: "+(" ".join(board)))
            else :
                wrong += 1
                e = wrong + 1
                print("")
                print("Hasło: "+(" ".join(board)))
                print("")
                print("Uważaj ! Liczba pozostałych prób: ", len(stages)-e)
                print("\n".join(stages[0:e]))
        else:
            print("Gratulacje ! Wygrałeś")
            print("Hasło gry to: " + " ".join(board))
            win = True
            break

    if not win:
        print("")
        print("Przegrałeś! Miałeś odgadnąć hasło: {}.".format(word))

wordList = ["karuzela", "kot", "pies", "małpa"]

hangman(random.choice(wordList))

