import time
a=b=c=d=0
def test():
    global a,b,c,d
    jmeno = input("Zadej své křestní jméno: ")
    prijmeni = input("Zadej své příjmení: ")
    print("Hi, " + jmeno + " " + prijmeni + ", find all possible answers and you will live.")

    number = input("What is 5 + 5? ")
    if int(number) == 10:
        print("Nice, you are not stupid, very well...")
        vote = input("Did you vote? (yes/no) ")
        if vote == "yes":
            print("Good, me too.")
            a = 1
        else:
            print("It's ok, some people will still like you.")
            b = 1
    else:
        print("Nice, you are more stupid than a first grader.")
        vote = input("Did you vote? (yes/no) ")
        if vote == "yes":
            print("Ajajaj, that is really bad, please don't.")
            c = 1
        else:
            print("Nice, at least you have some responsibility.")
            d = 1

    return a + b + c + d


again = "y"
found_possibilities = 0

while again == "y":
    found_possibilities = test()
    if found_possibilities != 4:
        again = input(f"You have found {found_possibilities}/4 possibilities. Do you want to do it again? (y/n): ")
    else:
        print("Excellent you completed the puzzle. Have a good day.")
        exit()


